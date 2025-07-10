#!/usr/bin/env python3
# Example module for a SR Linux subnet - aka a MAC VRF

import json
import eda_config as ecfg
from common.tunnelinterface import TunnelInterface

VXLAN_INTERFACE_INDEX = 0
ROUTE_DISTINGUISHER_DEFAULT = 1


class Subnet:
    def __init__(
            self,
            name,
            node,
            vlan,
            vlan_pool,
            subif_pool,
            evi,
            evi_pool,
            vni,
            vni_pool,
            interfaces,
            egress_filter,
            ingress_filter,
            import_target,
            export_target,
            tunnel_index_pool,
            mac_duplication=True,
            proxy_arp=False):
        self.name = name
        self.node = node
        self.vlan = vlan
        self.vlan_pool = vlan_pool
        self.subif_pool = subif_pool
        self.evi = evi
        self.evi_pool = evi_pool
        self.vni = vni
        self.vni_pool = vni_pool
        self.tunnel_index_pool = tunnel_index_pool
        self.interfaces = interfaces
        self.egress_filter = egress_filter
        self.ingress_filter = ingress_filter
        self.import_target = import_target
        self.export_target = export_target
        self.mac_duplication = mac_duplication
        self.proxy_arp = proxy_arp

    def get_path(self):
        return f'.network-instance{{.name=="{self.name}"}}'

    def get_config(self):
        configs = []
        sub_if_list = []
        for interface in self.interfaces:
            if not self.vlan:
                vlan_pool_obj = ecfg.Pool(name=self.vlan_pool, scope=f'{self.node}-{interface.replace("/", "-")}', type=ecfg.Pool.TYPE_INDEX)
                # interface_name = interface_cr['spec']['interface'].replace('/', '-')
                # print(f'Pool object for subnet: {vlan_pool_obj}, attempting to allocate with key sn-{self.name}')
                vlan = vlan_pool_obj.alloc(f'sn-{self.name}')
                # print(f'Got VLAN allocation: {vlan}')
            else:
                vlan = self.vlan
            subif_pool_obj = ecfg.Pool(name=self.subif_pool, scope=f'{self.node}-{interface.replace("/", "-")}', type=ecfg.Pool.TYPE_INDEX)
            subif_index = subif_pool_obj.alloc(f'sn-{self.name}')
            # else: vlan = self.vlan
            subif_config = {
                'admin-state': 'enable',
                'type': 'bridged',
                'vlan': {
                    'encap': {
                        'single-tagged': {
                            'vlan-id': vlan
                        }
                    }
                }
            }
            configs.append({
                "path": f'.interface{{.name=="{interface}"}}.subinterface{{.index=={subif_index}}}',
                "config": json.dumps(subif_config),
                "operation": "Create"})
            sub_if_list.append({'name': f'{interface}.{subif_index}'})

        if not self.vni:
            vni_pool = ecfg.Pool(name=self.vni_pool, scope='global', type=ecfg.Pool.TYPE_INDEX)
            vni = vni_pool.alloc(self.name)
        else:
            vni = self.vni
        if not self.evi:
            evi_pool = ecfg.Pool(name=self.evi_pool, scope='global', type=ecfg.Pool.TYPE_INDEX)
            evi = evi_pool.alloc(self.name)
        else:
            evi = self.evi
        tunnel_index_pool = ecfg.Pool(name=self.tunnel_index_pool, scope='global', type=ecfg.Pool.TYPE_INDEX)
        tunnel_index = tunnel_index_pool.alloc(self.name)
        tunnel_interface = f'vxlan{VXLAN_INTERFACE_INDEX}.{tunnel_index}'
        import_target = f'target:{ROUTE_DISTINGUISHER_DEFAULT}:{evi}' if not self.import_target else self.import_target
        export_target = f'target:{ROUTE_DISTINGUISHER_DEFAULT}:{evi}' if not self.export_target else self.export_target

        ti = TunnelInterface(index=tunnel_index, vni=vni, kind='bridged')

        config = {
            'type': 'mac-vrf',
            'admin-state': 'enable',
            'description': self.name,
            'interface': sub_if_list,
            'vxlan-interface': [
                {
                    'name': tunnel_interface
                }
            ],
            'protocols': {
                'bgp-evpn': {
                    'bgp-instance': [{
                        'id': 1,
                        'vxlan-interface': tunnel_interface,
                        'evi': evi,
                        'ecmp': 8
                    }]
                },
                'bgp-vpn': {
                    'bgp-instance': [{
                        'id': 1,
                        'route-target': {
                            'export-rt': export_target,
                            'import-rt': import_target
                        }
                    }]
                }
            }
        }
        if self.proxy_arp:
            config['bridge-table'] = {
                'proxy-arp': {
                    'admin-state': 'enable',
                    'dynamic-learning': {
                        'admin-state': 'enable',
                        'age-time': 600,
                        'send-refresh': 200
                    }
                }
            }
        if not self.mac_duplication:
            config['bridge-table']['mac-duplication'] = {
                'admin-state': 'disable'
            }
        configs.append({
            "path": self.get_path(),
            "config": json.dumps(config),
            "operation": "Create"})
        merged_config = configs + ti.get_config()
        return merged_config
