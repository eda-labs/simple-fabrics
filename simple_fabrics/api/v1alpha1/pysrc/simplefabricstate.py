#!/usr/bin/env python3
# Auto-generated classes based on your _types.go file (with special logic for CRDs that embed metav1.ObjectMeta)
# The change on this file will be overwritten by running edabuilder create or generate.
import eda_common as eda

from . import Metadata, Y_NAME

from simple_fabrics.api.v1alpha1.pysrc.constants import *
Y_FABRICNAME = 'fabricName'
# Package objects (GVK Schemas)
SIMPLEFABRICSTATE_SCHEMA = eda.Schema(group='simple-fabrics.eda.local', version='v1alpha1', kind='SimpleFabricState')


class SimpleFabricStateSpec:
    def __init__(
        self,
        fabricName: str,
    ):
        self.fabricName = fabricName

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.fabricName is not None:
            _rval[Y_FABRICNAME] = self.fabricName
        return _rval

    @staticmethod
    def from_input(obj) -> 'SimpleFabricStateSpec | None':
        if obj:
            _fabricName = obj.get(Y_FABRICNAME)
            return SimpleFabricStateSpec(
                fabricName=_fabricName,
            )
        return None  # pragma: no cover


class SimpleFabricStateStatus:
    def __init__(
        self,
    ):
        pass

    def to_input(self):  # pragma: no cover
        _rval = {}
        return _rval

    @staticmethod
    def from_input(obj) -> 'SimpleFabricStateStatus | None':
        if obj:
            return SimpleFabricStateStatus(
            )
        return None  # pragma: no cover


class SimpleFabricState:
    def __init__(
        self,
        metadata: Metadata | None = None,
        spec: SimpleFabricStateSpec | None = None,
        status: SimpleFabricStateStatus | None = None
    ):
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
    def from_input(obj) -> 'SimpleFabricState | None':
        if obj:
            _metadata = (
                Metadata.from_input(obj.get(Y_METADATA))
                if obj.get(Y_METADATA, None)
                else Metadata.from_name(obj.get(Y_NAME))
            )
            _spec = SimpleFabricStateSpec.from_input(obj.get(Y_SPEC, None))
            _status = SimpleFabricStateStatus.from_input(obj.get(Y_STATUS))
            return SimpleFabricState(
                metadata=_metadata,
                spec=_spec,
                status=_status,
            )
        return None  # pragma: no cover


class SimpleFabricStateList:
    def __init__(
        self,
        items: list[SimpleFabricState],
        listMeta: object | None = None
    ):
        self.items = items
        self.listMeta = listMeta

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.items is not None:
            _rval[Y_ITEMS] = self.items
        if self.listMeta is not None:
            _rval[Y_METADATA] = self.listMeta
        return _rval

    @staticmethod
    def from_input(obj) -> 'SimpleFabricStateList | None':
        if obj:
            _items = obj.get(Y_ITEMS, [])
            _listMeta = obj.get(Y_METADATA, None)
            return SimpleFabricStateList(
                items=_items,
                listMeta=_listMeta,
            )
        return None  # pragma: no cover
