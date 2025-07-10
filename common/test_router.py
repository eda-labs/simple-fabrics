#!/usr/bin/env python3
"""Unit tests for EDA Router module"""

import json
import eda_config as ec
import common_testing
import common.router_old as router

INPUT_SUBIF = "irb0"
INPUT_ROUTER_NAME = "test-router"
INPUT_SUBNET_NAME = "test-subnet"
INPUT_VNI = 4005
INPUT_VNI_POOL_NAME = "vni-pool"
INPUT_VNI_POOL_VALUE = 4001
INPUT_EVI = 4004
INPUT_EVI_POOL_NAME = "evi-pool"
INPUT_EVI_POOL_VALUE = 4002
INPUT_TUNNEL_INDEX_POOL_NAME = "tunnel-index-pool"
INPUT_TUNNEL_INDEX_POOL_VALUE = 4003
INPUT_INTERFACES = []
INPUT_EXPORT_TARGET = None
INPUT_IMPORT_TARGET = None


def setup_module():
    """Setup function"""
    ec.test_add_alloc(
        INPUT_VNI_POOL_NAME,
        "global",
        INPUT_ROUTER_NAME,
        INPUT_VNI_POOL_VALUE
    )
    ec.test_add_alloc(
        INPUT_EVI_POOL_NAME,
        "global",
        INPUT_ROUTER_NAME,
        INPUT_EVI_POOL_VALUE
    )
    ec.test_add_alloc(
        INPUT_TUNNEL_INDEX_POOL_NAME,
        "global",
        INPUT_ROUTER_NAME,
        INPUT_TUNNEL_INDEX_POOL_VALUE
    )


def teardown_module():
    """Teardown function"""
    ec.test_clear_all()


def test_routerattachment_sanity():
    """Sanity test for class RouterAttachment"""
    router_routerattachment = router.RouterAttachment(
        INPUT_SUBIF,
        INPUT_ROUTER_NAME,
        INPUT_SUBNET_NAME
    )
    assert isinstance(router_routerattachment, router.RouterAttachment)
    assert router_routerattachment.subif == INPUT_SUBIF
    assert router_routerattachment.router_name == INPUT_ROUTER_NAME
    assert router_routerattachment.subnet_name == INPUT_SUBNET_NAME
    assert len(router_routerattachment.get_config()) == 2
    router_routerattachment_get_config_list = [
        {
            'path': f'.network-instance{{.name=="{INPUT_ROUTER_NAME}"}}',
            'config': json.dumps({
                "interface": [
                    {
                        "name": f"{INPUT_SUBIF}"
                    }
                ]
            }),
            'operation': 'Update'
        },
        {
            'path': f'.network-instance{{.name=="{INPUT_SUBNET_NAME}"}}',
            'config': json.dumps({
                "interface": [
                    {
                        "name": f"{INPUT_SUBIF}"
                    }
                ]
            }),
            'operation': 'Update'
        }
    ]
    assert common_testing.compare_lists(router_routerattachment.get_config(), router_routerattachment_get_config_list) is True


def test_router_sanity_1():
    """Sanity test for class Router"""
    router_router = router.Router(
        INPUT_ROUTER_NAME,
        None,
        INPUT_VNI_POOL_NAME,
        None,
        INPUT_EVI_POOL_NAME,
        INPUT_TUNNEL_INDEX_POOL_NAME,
        INPUT_INTERFACES,
        INPUT_EXPORT_TARGET,
        INPUT_IMPORT_TARGET
    )
    assert isinstance(router_router, router.Router)
    assert router_router.name == INPUT_ROUTER_NAME
    assert router_router.vni_pool == INPUT_VNI_POOL_NAME
    assert router_router.vni is None
    assert router_router.evi_pool == INPUT_EVI_POOL_NAME
    assert router_router.evi is None
    assert router_router.tunnel_index_pool == INPUT_TUNNEL_INDEX_POOL_NAME
    assert router_router.interfaces == INPUT_INTERFACES
    assert router_router.export_target == INPUT_EXPORT_TARGET
    assert router_router.import_target == INPUT_IMPORT_TARGET
    assert len(router_router.get_config()) == 2
    router_router_get_config_list = [
        {
            'path': f'.network-instance{{.name=="{INPUT_ROUTER_NAME}"}}',
            'config': json.dumps({
                "type": "ip-vrf",
                "admin-state": "enable",
                "description": f"{INPUT_ROUTER_NAME}",
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
                                "ecmp": 8,
                                "routes": {
                                    "route-table": {
                                        "mac-ip": {
                                            "advertise-gateway-mac": True
                                        }
                                    }
                                }
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
                        "type": "routed",
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
    assert common_testing.compare_lists(router_router.get_config(), router_router_get_config_list) is True


def test_router_sanity_2():
    """Sanity test for class Router"""
    router_router = router.Router(
        INPUT_ROUTER_NAME,
        INPUT_VNI,
        None,
        INPUT_EVI,
        None,
        INPUT_TUNNEL_INDEX_POOL_NAME,
        INPUT_INTERFACES,
        INPUT_EXPORT_TARGET,
        INPUT_IMPORT_TARGET
    )
    assert isinstance(router_router, router.Router)
    assert router_router.name == INPUT_ROUTER_NAME
    assert router_router.vni_pool is None
    assert router_router.vni == INPUT_VNI
    assert router_router.evi_pool is None
    assert router_router.evi == INPUT_EVI
    assert router_router.tunnel_index_pool == INPUT_TUNNEL_INDEX_POOL_NAME
    assert router_router.interfaces == INPUT_INTERFACES
    assert router_router.export_target == INPUT_EXPORT_TARGET
    assert router_router.import_target == INPUT_IMPORT_TARGET
    assert len(router_router.get_config()) == 2
    router_router_get_config_list = [
        {
            'path': f'.network-instance{{.name=="{INPUT_ROUTER_NAME}"}}',
            'config': json.dumps({
                "type": "ip-vrf",
                "admin-state": "enable",
                "description": f"{INPUT_ROUTER_NAME}",
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
                                "ecmp": 8,
                                "routes": {
                                    "route-table": {
                                        "mac-ip": {
                                            "advertise-gateway-mac": True
                                        }
                                    }
                                }
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
                        "type": "routed",
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
    assert common_testing.compare_lists(router_router.get_config(), router_router_get_config_list) is True


if __name__ == "__main__":
    setup_module()
    test_routerattachment_sanity()
    test_router_sanity_1()
    test_router_sanity_2()
    teardown_module()
