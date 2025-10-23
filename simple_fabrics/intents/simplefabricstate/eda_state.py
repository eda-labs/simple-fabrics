#!/usr/bin/env python3
import eda_common as eda

import simple_fabrics.api.v1alpha1.pysrc.constants as c
from simple_fabrics.api.v1alpha1.pysrc.simplefabric import (
    SIMPLEFABRIC_SCHEMA,
    Metadata,
    SimpleFabric,
    SimpleFabricStatus,
)
from simple_fabrics.api.v1alpha1.pysrc.simplefabricstate import SimpleFabricState


class EdaStateHandler:
    def handle_cr(self, cr_obj: SimpleFabricState):
        sf = SimpleFabric(
            metadata=Metadata(
                name=cr_obj.metadata.name,
                namespace=cr_obj.metadata.namespace,
            ),
            status=SimpleFabricStatus(
                fabricName=cr_obj.spec.fabricName,
            ),
        )
        eda.update_cr(schema=SIMPLEFABRIC_SCHEMA, **sf.to_input())
