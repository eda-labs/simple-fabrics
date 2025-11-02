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
from utils.state import get_state_params


class EdaStateHandler:
    def handle_cr(self, cr_obj: SimpleFabricState):
        _oper_state = "UNKNOWN"
        fabric_path = f'.resources.cr.fabrics_eda_nokia_com.v1alpha1.fabric{{.name=="{cr_obj.spec.fabricName}"}}'

        fields = [
            "status.operationalState",
        ]
        fabric_cr_fields = get_state_params(fabric_path, fields, False)
        if not fabric_cr_fields or not isinstance(fabric_cr_fields, dict):
            return

        # Safely access nested dictionary with proper type checks
        status = fabric_cr_fields.get("status")
        if isinstance(status, dict):
            _oper_state = status.get("operationalState", "UNKNOWN")

        sf = SimpleFabric(
            metadata=Metadata(
                name=cr_obj.metadata.name,
                namespace=cr_obj.metadata.namespace,
            ),
            status=SimpleFabricStatus(fabricName=cr_obj.spec.fabricName, operationalState=_oper_state),
        )
        eda.update_cr(schema=SIMPLEFABRIC_SCHEMA, **sf.to_input())
