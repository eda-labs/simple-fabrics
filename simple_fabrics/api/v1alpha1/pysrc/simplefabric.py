#!/usr/bin/env python3
# Auto-generated classes based on your _types.go file (with special logic for CRDs that embed metav1.ObjectMeta)
# The change on this file will be overwritten by running edabuilder create or generate.
import eda_common as eda

from simple_fabrics.api.v1alpha1.pysrc.constants import Y_ITEMS, Y_METADATA, Y_SPEC, Y_STATUS

from . import Y_NAME, Metadata

Y_POD_NUMBER = "pod_number"
Y_LOCATION = "location"
Y_BAZ = "baz"
# Package objects (GVK Schemas)
SIMPLEFABRIC_SCHEMA = eda.Schema(group="simple-fabrics.eda.local", version="v1alpha1", kind="SimpleFabric")


class SimpleFabricSpec:
    def __init__(
        self,
        pod_number: str,
        location: str,
    ):
        self.pod_number = pod_number
        self.location = location

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.pod_number is not None:
            _rval[Y_POD_NUMBER] = self.pod_number
        if self.location is not None:
            _rval[Y_LOCATION] = self.location
        return _rval

    @staticmethod
    def from_input(obj) -> "SimpleFabricSpec | None":
        if obj:
            _pod_number = obj.get(Y_POD_NUMBER)
            _location = obj.get(Y_LOCATION)
            return SimpleFabricSpec(
                pod_number=_pod_number,
                location=_location,
            )
        return None  # pragma: no cover


class SimpleFabricStatus:
    def __init__(
        self,
        baz: str,
    ):
        self.baz = baz

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.baz is not None:
            _rval[Y_BAZ] = self.baz
        return _rval

    @staticmethod
    def from_input(obj) -> "SimpleFabricStatus | None":
        if obj:
            _baz = obj.get(Y_BAZ)
            return SimpleFabricStatus(
                baz=_baz,
            )
        return None  # pragma: no cover


class SimpleFabric:
    def __init__(self, metadata: Metadata, spec: SimpleFabricSpec, status: SimpleFabricStatus):
        self.metadata = metadata
        self.spec = spec
        self.status = status

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.metadata is not None:
            _rval[Y_NAME] = self.metadata.name
        if self.spec is not None:
            _rval[Y_SPEC] = self.spec.to_input()
        if self.status is not None:
            _rval[Y_STATUS] = self.status.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> "SimpleFabric | None":
        if obj:
            _metadata = (
                Metadata.from_input(obj.get(Y_METADATA))
                if obj.get(Y_METADATA, None)
                else Metadata.from_name(obj.get(Y_NAME))
            )
            _spec = SimpleFabricSpec.from_input(obj.get(Y_SPEC, None))
            _status = SimpleFabricStatus.from_input(obj.get(Y_STATUS))
            return SimpleFabric(
                metadata=_metadata,
                spec=_spec,
                status=_status,
            )
        return None  # pragma: no cover


class SimpleFabricList:
    def __init__(self, listMeta: object, items: list[SimpleFabric]):
        self.listMeta = listMeta
        self.items = items

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.listMeta is not None:
            _rval[Y_METADATA] = self.listMeta
        if self.items is not None:
            _rval[Y_ITEMS] = self.items
        return _rval

    @staticmethod
    def from_input(obj) -> "SimpleFabricList | None":
        if obj:
            _listMeta = obj.get(Y_METADATA, None)
            _items = obj.get(Y_ITEMS, [])
            return SimpleFabricList(
                listMeta=_listMeta,
                items=_items,
            )
        return None  # pragma: no cover
