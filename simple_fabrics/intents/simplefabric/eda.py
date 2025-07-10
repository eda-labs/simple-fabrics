#!/usr/bin/env python3
import json

import eda_common as eda
import eda_config as ecfg

import utils.schema as s
from common.metadata import Y_METADATA, Y_NAME
from simple_fabrics.api.v1alpha1.pysrc.simplefabric import SimpleFabric


class EDAConfigHandler:
    def handle_cr(self, sf: SimpleFabric):
        fabric_spec = {
            "interSwitchLinks": {"linkSelector": ["eda.nokia.com/role=interSwitch"], "unnumbered": "IPV6"},
            "leafs": {"leafNodeSelector": ["eda.nokia.com/role=leaf"]},
            "overlayProtocol": {"protocol": "EBGP"},
            "spines": {"spineNodeSelector": ["eda.nokia.com/role=spine"]},
            "systemPoolIPV4": "systemipv4-pool",
            "underlayProtocol": {"bgp": {"asnPool": "asn-pool"}, "protocol": ["EBGP"]},
        }
        eda.update_cr(
            schema=s.FABRIC_SCHEMA,
            name=f"{sf.metadata.name}-{sf.spec.location}-{sf.spec.pod_number}",
            spec=fabric_spec,
        )
