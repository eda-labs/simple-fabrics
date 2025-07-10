#!/usr/bin/env python3
# Module for a SR Linux tunnel interface

import json

VXLAN_INTERFACE_INDEX = 0


class TunnelInterface:
    def __init__(self, index, vni, kind):
        self.index = index
        self.vni = vni
        self.kind = kind

    def get_config(self):
        configs = []
        config = {
            'vxlan-interface': [{
                'index': self.index,
                'type': self.kind,
                'ingress': {
                    'vni': self.vni
                },
                'egress': {
                    'source-ip': 'use-system-ipv4-address'
                }
            }]
        }
        configs.append({"path": f'.tunnel-interface{{.name=="vxlan{VXLAN_INTERFACE_INDEX}"}}',
                        "config": json.dumps(config),
                        "operation": "Create"})
        return configs
