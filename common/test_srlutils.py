#!/usr/bin/env python3

import json
from common import srlutils
from common_testing import compare_common


class IpAddress:
    def __init__(self, ipPrefix: str, primary: bool = False) -> None:
        self.ipPrefix = ipPrefix
        self.primary = primary


def test_get_subif_ipv4_config_sanity_1():
    val_ipv4_address = '1.1.1.1'
    val_anycast = True
    val_learn_unsolicited = True
    result = srlutils.get_subif_ipv4_config(
        ip_addresses=[IpAddress(val_ipv4_address, primary=True)],
        host_route=True,
        learn_unsolicited=val_learn_unsolicited,
        anycast=val_anycast,
        irb=True
    )
    expected_result = {
        "admin-state": "enable",
        "address": [
            {
                "ip-prefix": val_ipv4_address,
                "primary": "",
                "anycast-gw": val_anycast
            }
        ],
        "arp": {
            "evpn": {
                "advertise": [
                    {
                        "route-type": "dynamic"
                    },
                    {
                        "route-type": "static"
                    }
                ]
            },
            "host-route": {
                "populate": [
                    {
                        "route-type": "dynamic"
                    }
                ]
            },
            "learn-unsolicited": val_learn_unsolicited
        }
    }
    assert compare_common(result, expected_result) is True


def test_get_subif_ipv4_config_sanity_2():
    result = srlutils.get_subif_ipv4_config(
        ip_addresses=[]
    )
    expected_result = {}
    assert compare_common(result, expected_result) is True


def test_get_subif_ipv6_config_sanity_1():
    val_ipv6_address = '3ffe:abcd::12'
    val_anycast = True
    result = srlutils.get_subif_ipv6_config(
        ip_addresses=[IpAddress(val_ipv6_address, primary=True)],
        anycast=val_anycast,
        irb=True
    )
    expected_result = {
        "admin-state": "enable",
        "address": [
            {
                "ip-prefix": val_ipv6_address,
                "primary": "",
                "anycast-gw": val_anycast
            }
        ],
        "neighbor-discovery": {
            "evpn": {
                "advertise": [
                    {
                        "route-type": "dynamic"
                    },
                    {
                        "route-type": "static"
                    }
                ]
            }
        }
    }
    assert compare_common(result, expected_result) is True


def test_get_subif_ipv6_config_sanity_2():
    result = srlutils.get_subif_ipv6_config(
        ip_addresses=[],
    )
    expected_result = {}
    assert compare_common(result, expected_result) is True


def test_get_router_intf_attachment_config_sanity():
    val_intf_name = 'ethernet-1/1'
    val_router_name = 'router0'
    result = srlutils.get_router_intf_attachment_config(
        val_intf_name,
        val_router_name
    )
    expected_result = {
        "path": f'.network-instance{{.name=="{val_router_name}"}}',
        "config": json.dumps({
            "interface": [
                {
                    "name": val_intf_name
                }
            ]
        }),
        "operation": "Update"
    }
    assert compare_common(result, expected_result) is True


def test_get_vxlan_if_config_sanity():
    val_tunnel_index = 1000
    val_vni = 2000
    val_type = 'bridged'
    result = srlutils.get_vxlan_if_config(
        val_tunnel_index,
        val_vni,
        val_type
    )
    expected_result = {
        'path': '.tunnel-interface{.name=="vxlan0"}',
        'config': json.dumps({
            'vxlan-interface': [
                {
                    'index': val_tunnel_index,
                    'type': val_type,
                    'ingress': {
                        'vni': val_vni
                    },
                    'egress': {
                        'source-ip': 'use-system-ipv4-address'
                    }
                }
            ]
        }),
        'operation': 'Create'
    }

    assert compare_common(result, expected_result) is True


if __name__ == '__main__':
    test_get_subif_ipv4_config_sanity_1()
    test_get_subif_ipv4_config_sanity_2()
    test_get_subif_ipv6_config_sanity_1()
    test_get_subif_ipv6_config_sanity_2()
    test_get_router_intf_attachment_config_sanity()
    test_get_vxlan_if_config_sanity()
