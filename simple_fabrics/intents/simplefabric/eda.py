#!/usr/bin/env python3

import eda_common as eda

import simple_fabrics.deps.fabrics_eda_nokia_com.v4_0_1.api.v1alpha1.pysrc.fabric as fabric
from simple_fabrics.api.v1alpha1.pysrc.simplefabric import SimpleFabric


class EDAConfigHandler:
    def handle_cr(self, sf: SimpleFabric):
        fabricName = f"sf-{sf.metadata.name}"

        _fabric = fabric.Fabric(
            metadata=fabric.Metadata(
                name=fabricName,
                namespace=sf.metadata.namespace,
            ),
            spec=fabric.FabricSpec(
                leafs=fabric.Leafs(
                    leafNodeSelector=["eda.nokia.com/role=leaf"],
                ),
                spines=fabric.Spines(
                    spineNodeSelector=["eda.nokia.com/role=spine"],
                ),
                interSwitchLinks=fabric.InterSwitchLinks(
                    linkSelector=["eda.nokia.com/role=interSwitch"],
                    unnumbered="IPV6",
                ),
                systemPoolIPV4="systemipv4-pool",
                underlayProtocol=fabric.UnderlayProtocol(
                    bgp=fabric.UnderlayBGP(asnPool=sf.spec.underlayASNPool),
                    protocol=["EBGP"],
                ),
                overlayProtocol=fabric.OverlayProtocol(
                    protocol="EBGP",
                ),
            ),
        )

        eda.update_cr(schema=fabric.FABRIC_SCHEMA, **_fabric.to_input())
