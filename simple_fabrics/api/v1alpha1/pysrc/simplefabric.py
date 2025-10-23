#!/usr/bin/env python3
# Auto-generated classes based on your _types.go file (with special logic for CRDs that embed metav1.ObjectMeta)
# The change on this file will be overwritten by running edabuilder create or generate.
import eda_common as eda

from . import Metadata, Y_NAME

from simple_fabrics.api.v1alpha1.pysrc.constants import *
Y_UNDERLAYASNPOOL = 'underlayASNPool'
Y_FABRICNAME = 'fabricName'
# Package objects (GVK Schemas)
SIMPLEFABRIC_SCHEMA = eda.Schema(group='simple-fabrics.eda.local', version='v1alpha1', kind='SimpleFabric')


class SimpleFabricSpec:
    def __init__(
        self,
        underlayASNPool: str,
    ):
        self.underlayASNPool = underlayASNPool

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.underlayASNPool is not None:
            _rval[Y_UNDERLAYASNPOOL] = self.underlayASNPool
        return _rval

    @staticmethod
    def from_input(obj) -> 'SimpleFabricSpec | None':
        if obj:
            _underlayASNPool = obj.get(Y_UNDERLAYASNPOOL, "asn-pool")
            return SimpleFabricSpec(
                underlayASNPool=_underlayASNPool,
            )
        return None  # pragma: no cover


class SimpleFabricStatus:
    def __init__(
        self,
        fabricName: str | None = None,
    ):
        self.fabricName = fabricName

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.fabricName is not None:
            _rval[Y_FABRICNAME] = self.fabricName
        return _rval

    @staticmethod
    def from_input(obj) -> 'SimpleFabricStatus | None':
        if obj:
            _fabricName = obj.get(Y_FABRICNAME)
            return SimpleFabricStatus(
                fabricName=_fabricName,
            )
        return None  # pragma: no cover


class SimpleFabric:
    def __init__(
        self,
        metadata: Metadata | None = None,
        spec: SimpleFabricSpec | None = None,
        status: SimpleFabricStatus | None = None
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
    def from_input(obj) -> 'SimpleFabric | None':
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
    def __init__(
        self,
        items: list[SimpleFabric],
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
    def from_input(obj) -> 'SimpleFabricList | None':
        if obj:
            _items = obj.get(Y_ITEMS, [])
            _listMeta = obj.get(Y_METADATA, None)
            return SimpleFabricList(
                items=_items,
                listMeta=_listMeta,
            )
        return None  # pragma: no cover
