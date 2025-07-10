#!/usr/bin/env python3
"""Unit tests for eda Subnet module"""

import json
import common_testing
import eda_config as ec
from common.subnet_old import Subnet

INPUT_NAME = "test-subnet"
INPUT_NODE = "dut1"
INPUT_VLAN = 4004
INPUT_VLAN_POOL_NAME = "vlan-pool"
INPUT_VLAN_POOL_VALUE = 4007
INPUT_SUBIF_POOL_NAME = "subif-pool"
INPUT_SUBIF_POOL_VALUE = 4008
INPUT_EVI = 4005
INPUT_EVI_POOL_NAME = "evi-pool"
INPUT_EVI_POOL_VALUE = 4002
INPUT_VNI = 4006
INPUT_VNI_POOL_NAME = "vni-pool"
INPUT_VNI_POOL_VALUE = 4001
INPUT_INTERFACE_NAME = 'ethernet-1/1'
INPUT_INTERFACES = [
    INPUT_INTERFACE_NAME
]
INPUT_EGRESS_FILTER = None
INPUT_INGRESS_FILTER = None
INPUT_IMPORT_TARGET = None
INPUT_EXPORT_TARGET = None
INPUT_TUNNEL_INDEX_POOL_NAME = "tunnel-index-pool"
INPUT_TUNNEL_INDEX_POOL_VALUE = 4003
INPUT_MAC_DUPLICATION = False
INPUT_PROXY_ARP = True


def setup_module():
    """Setup function"""
    ec.test_add_alloc(
        INPUT_VNI_POOL_NAME,
        "global",
        INPUT_NAME,
        INPUT_VNI_POOL_VALUE
    )
    ec.test_add_alloc(
        INPUT_EVI_POOL_NAME,
        "global",
        INPUT_NAME,
        INPUT_EVI_POOL_VALUE
    )
    ec.test_add_alloc(
        INPUT_TUNNEL_INDEX_POOL_NAME,
        "global",
        INPUT_NAME,
        INPUT_TUNNEL_INDEX_POOL_VALUE
    )
    ec.test_add_alloc(
        INPUT_VLAN_POOL_NAME,
        f"{INPUT_NODE}-{INPUT_INTERFACE_NAME.replace('/', '-')}",
        f"sn-{INPUT_NAME}",
        INPUT_VLAN_POOL_VALUE
    )
    ec.test_add_alloc(
        INPUT_SUBIF_POOL_NAME,
        f"{INPUT_NODE}-{INPUT_INTERFACE_NAME.replace('/', '-')}",
        f"sn-{INPUT_NAME}",
        INPUT_SUBIF_POOL_VALUE
    )


def teardown_module():
    """Teardown function"""
    ec.test_clear_all()


def test_subnet_sanity_1():
    """Sanity test for class Subnet"""
    subnet_subnet = Subnet(
        INPUT_NAME,
        INPUT_NODE,
        None,
        INPUT_VLAN_POOL_NAME,
        INPUT_SUBIF_POOL_NAME,
        None,
        INPUT_EVI_POOL_NAME,
        None,
        INPUT_VNI_POOL_NAME,
        INPUT_INTERFACES,
        INPUT_EGRESS_FILTER,
        INPUT_INGRESS_FILTER,
        INPUT_IMPORT_TARGET,
        INPUT_EXPORT_TARGET,
        INPUT_TUNNEL_INDEX_POOL_NAME,
        INPUT_MAC_DUPLICATION,
        INPUT_PROXY_ARP
    )
    assert isinstance(subnet_subnet, Subnet)
    assert subnet_subnet.name == INPUT_NAME
    assert subnet_subnet.node == INPUT_NODE
    assert subnet_subnet.vlan is None
    assert subnet_subnet.vlan_pool == INPUT_VLAN_POOL_NAME
    assert subnet_subnet.subif_pool == INPUT_SUBIF_POOL_NAME
    assert subnet_subnet.evi is None
    assert subnet_subnet.evi_pool == INPUT_EVI_POOL_NAME
    assert subnet_subnet.vni is None
    assert subnet_subnet.vni_pool == INPUT_VNI_POOL_NAME
    assert subnet_subnet.tunnel_index_pool == INPUT_TUNNEL_INDEX_POOL_NAME
    assert subnet_subnet.interfaces == INPUT_INTERFACES
    assert subnet_subnet.egress_filter == INPUT_EGRESS_FILTER
    assert subnet_subnet.ingress_filter == INPUT_INGRESS_FILTER
    assert subnet_subnet.import_target == INPUT_IMPORT_TARGET
    assert subnet_subnet.export_target == INPUT_EXPORT_TARGET
    assert subnet_subnet.mac_duplication == INPUT_MAC_DUPLICATION
    assert subnet_subnet.proxy_arp == INPUT_PROXY_ARP
    assert len(subnet_subnet.get_config()) == 3
    subnet_subnet_get_config_list = [
        {
            'path': f'.interface{{.name=="{INPUT_INTERFACE_NAME}"}}.subinterface{{.index=={INPUT_SUBIF_POOL_VALUE}}}',
            'config': json.dumps({
                "admin-state": "enable",
                "type": "bridged",
                "vlan": {
                    "encap": {
                        "single-tagged": {
                            "vlan-id": INPUT_VLAN_POOL_VALUE
                        }
                    }
                }
            }),
            'operation': 'Create'
        },
        {
            'path': f'.network-instance{{.name=="{INPUT_NAME}"}}',
            'config': json.dumps({
                "type": "mac-vrf",
                "admin-state": "enable",
                "description": INPUT_NAME,
                "interface": [
                    {
                        "name": f"{INPUT_INTERFACE_NAME}.{INPUT_SUBIF_POOL_VALUE}"
                    }
                ],
                "vxlan-interface": [
                    {
                        "name": f"vxlan0.{INPUT_TUNNEL_INDEX_POOL_VALUE}"
                    }
                ],
                "protocols": {
                    "bgp-evpn": {
                        "bgp-instance": [
                            {
                                "id": 1,
                                "vxlan-interface": f"vxlan0.{INPUT_TUNNEL_INDEX_POOL_VALUE}",
                                "evi": INPUT_EVI_POOL_VALUE,
                                "ecmp": 8
                            }
                        ]
                    },
                    "bgp-vpn": {
                        "bgp-instance": [
                            {
                                "id": 1,
                                "route-target": {
                                    "export-rt": f"target:1:{INPUT_EVI_POOL_VALUE}",
                                    "import-rt": f"target:1:{INPUT_EVI_POOL_VALUE}"
                                }
                            }
                        ]
                    }
                },
                "bridge-table": {
                    "proxy-arp": {
                        "admin-state": "enable",
                        "dynamic-learning": {
                            "admin-state": "enable",
                            "age-time": 600,
                            "send-refresh": 200
                        }
                    },
                    "mac-duplication": {
                        "admin-state": "disable"
                    }
                }
            }),
            'operation': 'Create'
        },
        {
            'path': '.tunnel-interface{.name=="vxlan0"}',
            'config': json.dumps({
                "vxlan-interface": [
                    {
                        "index": INPUT_TUNNEL_INDEX_POOL_VALUE,
                        "type": "bridged",
                        "ingress": {
                            "vni": INPUT_VNI_POOL_VALUE
                        },
                        "egress": {
                            "source-ip": "use-system-ipv4-address"
                        }
                    }
                ]
            }),
            'operation': 'Create'
        }
    ]
    assert common_testing.compare_common(subnet_subnet.get_config(), subnet_subnet_get_config_list) is True


def test_subnet_sanity_2():
    """Sanity test for class Subnet"""
    subnet_subnet = Subnet(
        INPUT_NAME,
        INPUT_NODE,
        INPUT_VLAN,
        None,
        INPUT_SUBIF_POOL_NAME,
        INPUT_EVI,
        None,
        INPUT_VNI,
        None,
        INPUT_INTERFACES,
        INPUT_EGRESS_FILTER,
        INPUT_INGRESS_FILTER,
        INPUT_IMPORT_TARGET,
        INPUT_EXPORT_TARGET,
        INPUT_TUNNEL_INDEX_POOL_NAME,
        INPUT_MAC_DUPLICATION,
        INPUT_PROXY_ARP
    )
    assert isinstance(subnet_subnet, Subnet)
    assert subnet_subnet.name == INPUT_NAME
    assert subnet_subnet.node == INPUT_NODE
    assert subnet_subnet.vlan == INPUT_VLAN
    assert subnet_subnet.vlan_pool is None
    assert subnet_subnet.subif_pool == INPUT_SUBIF_POOL_NAME
    assert subnet_subnet.evi == INPUT_EVI
    assert subnet_subnet.evi_pool is None
    assert subnet_subnet.vni == INPUT_VNI
    assert subnet_subnet.vni_pool is None
    assert subnet_subnet.tunnel_index_pool == INPUT_TUNNEL_INDEX_POOL_NAME
    assert subnet_subnet.interfaces == INPUT_INTERFACES
    assert subnet_subnet.egress_filter == INPUT_EGRESS_FILTER
    assert subnet_subnet.ingress_filter == INPUT_INGRESS_FILTER
    assert subnet_subnet.import_target == INPUT_IMPORT_TARGET
    assert subnet_subnet.export_target == INPUT_EXPORT_TARGET
    assert subnet_subnet.mac_duplication == INPUT_MAC_DUPLICATION
    assert subnet_subnet.proxy_arp == INPUT_PROXY_ARP
    assert len(subnet_subnet.get_config()) == 3
    subnet_subnet_get_config_list = [
        {
            'path': f'.interface{{.name=="{INPUT_INTERFACE_NAME}"}}.subinterface{{.index=={INPUT_SUBIF_POOL_VALUE}}}',
            'config': json.dumps({
                "admin-state": "enable",
                "type": "bridged",
                "vlan": {
                    "encap": {
                        "single-tagged": {
                            "vlan-id": INPUT_VLAN
                        }
                    }
                }
            }),
            'operation': 'Create'
        },
        {
            'path': f'.network-instance{{.name=="{INPUT_NAME}"}}',
            'config': json.dumps({
                "type": "mac-vrf",
                "admin-state": "enable",
                "description": INPUT_NAME,
                "interface": [
                    {
                        "name": f"{INPUT_INTERFACE_NAME}.{INPUT_SUBIF_POOL_VALUE}"
                    }
                ],
                "vxlan-interface": [
                    {
                        "name": f"vxlan0.{INPUT_TUNNEL_INDEX_POOL_VALUE}"
                    }
                ],
                "protocols": {
                    "bgp-evpn": {
                        "bgp-instance": [
                            {
                                "id": 1,
                                "vxlan-interface": f"vxlan0.{INPUT_TUNNEL_INDEX_POOL_VALUE}",
                                "evi": INPUT_EVI,
                                "ecmp": 8
                            }
                        ]
                    },
                    "bgp-vpn": {
                        "bgp-instance": [
                            {
                                "id": 1,
                                "route-target": {
                                    "export-rt": f"target:1:{INPUT_EVI}",
                                    "import-rt": f"target:1:{INPUT_EVI}"
                                }
                            }
                        ]
                    }
                },
                "bridge-table": {
                    "proxy-arp": {
                        "admin-state": "enable",
                        "dynamic-learning": {
                            "admin-state": "enable",
                            "age-time": 600,
                            "send-refresh": 200
                        }
                    },
                    "mac-duplication": {
                        "admin-state": "disable"
                    }
                }
            }),
            'operation': 'Create'
        },
        {
            'path': '.tunnel-interface{.name=="vxlan0"}',
            'config': json.dumps({
                "vxlan-interface": [
                    {
                        "index": INPUT_TUNNEL_INDEX_POOL_VALUE,
                        "type": "bridged",
                        "ingress": {
                            "vni": INPUT_VNI
                        },
                        "egress": {
                            "source-ip": "use-system-ipv4-address"
                        }
                    }
                ]
            }),
            'operation': 'Create'
        }
    ]
    assert common_testing.compare_common(subnet_subnet.get_config(), subnet_subnet_get_config_list) is True


if __name__ == "__main__":
    setup_module()
    test_subnet_sanity_1()
    test_subnet_sanity_2()
    teardown_module()
