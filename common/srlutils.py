#!/usr/bin/env python3

import json
from common.constants import DEFAULT_VXLAN_IF_INDEX


def get_subif_ipv4_config(
        ip_addresses,
        host_route=False,
        learn_unsolicited=False,
        anycast=False,
        irb=False):
    conf = {}
    ip_addresses_conf = build_address_config(ip_addresses=ip_addresses, anycast=anycast)
    if len(ip_addresses_conf) == 0:
        return {}
    conf['admin-state'] = 'enable'
    conf['address'] = ip_addresses_conf
    if irb:
        conf['arp'] = {
            'evpn': {
                'advertise': [
                    {
                        'route-type': 'dynamic'
                    },
                    {
                        'route-type': 'static'
                    }
                ]
            }
        }
    if host_route:
        conf['arp']['host-route'] = {
            'populate': [
                {
                    'route-type': 'dynamic'
                }
            ]
        }
    if learn_unsolicited:
        conf['arp']['learn-unsolicited'] = True
    return conf


def get_subif_ipv6_config(
        ip_addresses,
        anycast=False,
        irb=False):
    conf = {}
    ip_addresses_conf = build_address_config(ip_addresses=ip_addresses, anycast=anycast)
    if len(ip_addresses_conf) == 0:
        return {}
    conf['admin-state'] = 'enable'
    conf['address'] = ip_addresses_conf
    if irb:
        conf['neighbor-discovery'] = {
            'evpn': {
                'advertise': [
                    {
                        'route-type': 'dynamic'
                    },
                    {
                        'route-type': 'static'
                    }
                ]
            }
        }
    return conf


def build_address_config(ip_addresses, anycast=False):
    ip_addresses_conf = []
    for address in ip_addresses:
        add_cfg = {'ip-prefix': address.ipPrefix}
        if address.primary:
            add_cfg['primary'] = ''
        if anycast:
            add_cfg['anycast-gw'] = True
        ip_addresses_conf.append(add_cfg)
    return ip_addresses_conf


def get_router_intf_attachment_config(intf_name, router_name):
    # router attachment.
    ni_cfg = {
        'interface': [{
            'name': intf_name
        }]
    }
    return {"path": f'.network-instance{{.name=="{router_name}"}}',
            "config": json.dumps(ni_cfg),
            "operation": "Update"}


def get_vxlan_if_config(tunnel_index, vni, type):
    ti_config = {
        'vxlan-interface': [{
            'index': tunnel_index,
            'type': type,
            'ingress': {
                'vni': vni
            },
            'egress': {
                'source-ip': 'use-system-ipv4-address'
            }
        }]
    }
    return {"path": f'.tunnel-interface{{.name=="vxlan{DEFAULT_VXLAN_IF_INDEX}"}}',
            "config": json.dumps(ti_config),
            "operation": "Create"}
