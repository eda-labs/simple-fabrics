#!/usr/bin/env python3
# Example module for a SR Linux Router - aka an IP VRF
import json
import eda_config as ec
from common.tunnelinterface import TunnelInterface

VXLAN_INTERFACE_INDEX = 0
ROUTE_DISTINGUISHER_DEFAULT = 1


class RouterAttachment:
    def __init__(self, subif, router_name, subnet_name=None):
        self.subif = subif
        self.router_name = router_name
        self.subnet_name = subnet_name

    def get_config(self):
        configs = []
        # router_config = {
        #     'interface': [{
        #         'name': self.subif
        #     }]
        # }
        # configs.append({"path": f'.network-instance{{.name=="{self.router_name}}}"',
        #                 "config": json.dumps(router_config),
        #                 "operation": "Update"})
        router_config = {
            'interface': [{
                'name': self.subif
            }]
        }
        configs.append({"path": f'.network-instance{{.name=="{self.router_name}"}}',
                        "config": json.dumps(router_config),
                        "operation": "Update"})
        if self.subnet_name:
            subnet_config = {
                'interface': [{
                    'name': self.subif
                }]
            }
            configs.append({"path": f'.network-instance{{.name=="{self.subnet_name}"}}',
                            "config": json.dumps(subnet_config),
                            "operation": "Update"})
        return configs


class Router:
    def __init__(
            self,
            name,
            vni,
            vni_pool,
            evi,
            evi_pool,
            tunnel_index_pool,
            interfaces,
            export_target,
            import_target):
        self.name = name
        self.vni_pool = vni_pool
        self.vni = vni
        self.evi_pool = evi_pool
        self.evi = evi
        self.tunnel_index_pool = tunnel_index_pool
        self.interfaces = interfaces
        self.export_target = export_target
        self.import_target = import_target

    def get_path(self):
        return f'.network-instance{{.name=="{self.name}"}}'

    def get_config(self):
        configs = []
        if not self.vni:
            vni_pool = ec.Pool(name=self.vni_pool, scope='global', type=ec.Pool.TYPE_INDEX)
            vni = vni_pool.alloc(self.name)
        else:
            vni = self.vni
        if not self.evi:
            evi_pool = ec.Pool(name=self.evi_pool, scope='global', type=ec.Pool.TYPE_INDEX)
            evi = evi_pool.alloc(self.name)
        else:
            evi = self.evi
        tunnel_index_pool = ec.Pool(name=self.tunnel_index_pool, scope='global', type=ec.Pool.TYPE_INDEX)
        tunnel_index = tunnel_index_pool.alloc(self.name)
        tunnel_interface = f'vxlan{VXLAN_INTERFACE_INDEX}.{tunnel_index}'
        ti = TunnelInterface(index=tunnel_index, vni=vni, kind='routed')
        import_target = f'target:{ROUTE_DISTINGUISHER_DEFAULT}:{evi}' if not self.import_target else self.import_target
        export_target = f'target:{ROUTE_DISTINGUISHER_DEFAULT}:{evi}' if not self.export_target else self.export_target

        config = {
            'type': 'ip-vrf',
            'admin-state': 'enable',
            'description': self.name,
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
                        'ecmp': 8,
                        'routes': {
                            'route-table': {
                                'mac-ip': {
                                    'advertise-gateway-mac': True
                                }
                            }
                        }
                    }]
                },
                'bgp-vpn': {
                    'bgp-instance': [
                        {
                            'id': 1,
                            'route-target': {
                                'export-rt': export_target,
                                'import-rt': import_target
                            }
                        }
                    ]
                }
            }
        }
        configs.append({
            "path": self.get_path(),
            "config": json.dumps(config),
            "operation": "Create"})
        merged_config = configs + ti.get_config()
        return merged_config
