#!/usr/bin/env python3
"""Unit tests for eda TunnelInterface module"""

import json
from common import tunnelinterface

INPUT_INDEX = 1
INPUT_VNI = 2
INPUT_KIND = "bridged"


def test_tunnelinterface_sanity():
    """Sanity test for class TunnelInterface"""
    tunnelinterface_tunnelinterface = tunnelinterface.TunnelInterface(
        INPUT_INDEX,
        INPUT_VNI,
        INPUT_KIND
    )
    assert isinstance(tunnelinterface_tunnelinterface, tunnelinterface.TunnelInterface)
    assert tunnelinterface_tunnelinterface.index == INPUT_INDEX
    assert tunnelinterface_tunnelinterface.vni == INPUT_VNI
    assert tunnelinterface_tunnelinterface.kind == INPUT_KIND
    assert len(tunnelinterface_tunnelinterface.get_config()) == 1
    assert tunnelinterface_tunnelinterface.get_config()[0]['path'] == '.tunnel-interface{.name=="vxlan0"}'
    assert json.loads(tunnelinterface_tunnelinterface.get_config()[0]['config']) == {
        "vxlan-interface": [
            {
                "index": INPUT_INDEX,
                "type": INPUT_KIND,
                "ingress": {
                    "vni": INPUT_VNI
                },
                "egress": {
                    "source-ip": "use-system-ipv4-address"
                }
            }
        ]
    }
    assert tunnelinterface_tunnelinterface.get_config()[0]['operation'] == 'Create'


if __name__ == "__main__":
    test_tunnelinterface_sanity()
