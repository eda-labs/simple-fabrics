#!/usr/bin/env python3
# Auto-generated classes based on your _types.go file (with special logic for CRDs that embed metav1.ObjectMeta)
# The change on this file will be overwritten by running edabuilder create or generate.
import eda_common as eda

from . import Y_NAME, Metadata
from .constants import *
from .fabric import Node

Y_BORDERLEAFNODES = "borderLeafNodes"
Y_LEAFNODES = "leafNodes"
Y_SPINENODES = "spineNodes"
Y_SUPERSPINENODES = "superSpineNodes"
Y_ISLS = "isls"
Y_DEFAULTROUTERS = "defaultRouters"
# Package objects (GVK Schemas)
FABRICSTATE_SCHEMA = eda.Schema(group="fabrics.eda.nokia.com", version="v1alpha1", kind="FabricState")


class FabricStateSpec:
    def __init__(
        self,
        borderLeafNodes: list[Node] | None = None,
        leafNodes: list[Node] | None = None,
        spineNodes: list[Node] | None = None,
        superSpineNodes: list[Node] | None = None,
        isls: list[str] | None = None,
        defaultRouters: list[str] | None = None,
    ):
        self.borderLeafNodes = borderLeafNodes
        self.leafNodes = leafNodes
        self.spineNodes = spineNodes
        self.superSpineNodes = superSpineNodes
        self.isls = isls
        self.defaultRouters = defaultRouters

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.borderLeafNodes is not None:
            _rval[Y_BORDERLEAFNODES] = [x.to_input() for x in self.borderLeafNodes]
        if self.leafNodes is not None:
            _rval[Y_LEAFNODES] = [x.to_input() for x in self.leafNodes]
        if self.spineNodes is not None:
            _rval[Y_SPINENODES] = [x.to_input() for x in self.spineNodes]
        if self.superSpineNodes is not None:
            _rval[Y_SUPERSPINENODES] = [x.to_input() for x in self.superSpineNodes]
        if self.isls is not None:
            _rval[Y_ISLS] = self.isls
        if self.defaultRouters is not None:
            _rval[Y_DEFAULTROUTERS] = self.defaultRouters
        return _rval

    @staticmethod
    def from_input(obj) -> "FabricStateSpec | None":
        if obj:
            _borderLeafNodes = []
            if obj.get(Y_BORDERLEAFNODES) is not None:
                for x in obj.get(Y_BORDERLEAFNODES):
                    _borderLeafNodes.append(Node.from_input(x))
            _leafNodes = []
            if obj.get(Y_LEAFNODES) is not None:
                for x in obj.get(Y_LEAFNODES):
                    _leafNodes.append(Node.from_input(x))
            _spineNodes = []
            if obj.get(Y_SPINENODES) is not None:
                for x in obj.get(Y_SPINENODES):
                    _spineNodes.append(Node.from_input(x))
            _superSpineNodes = []
            if obj.get(Y_SUPERSPINENODES) is not None:
                for x in obj.get(Y_SUPERSPINENODES):
                    _superSpineNodes.append(Node.from_input(x))
            _isls = obj.get(Y_ISLS)
            _defaultRouters = obj.get(Y_DEFAULTROUTERS)
            return FabricStateSpec(
                borderLeafNodes=_borderLeafNodes,
                leafNodes=_leafNodes,
                spineNodes=_spineNodes,
                superSpineNodes=_superSpineNodes,
                isls=_isls,
                defaultRouters=_defaultRouters,
            )
        return None  # pragma: no cover


class FabricStateStatus:
    def __init__(
        self,
    ):
        pass

    def to_input(self):  # pragma: no cover
        _rval = {}
        return _rval

    @staticmethod
    def from_input(obj) -> "FabricStateStatus | None":
        if obj:
            return FabricStateStatus()
        return None  # pragma: no cover


class FabricState:
    def __init__(
        self,
        metadata: Metadata | None = None,
        spec: FabricStateSpec | None = None,
        status: FabricStateStatus | None = None,
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
    def from_input(obj) -> "FabricState | None":
        if obj:
            _metadata = (
                Metadata.from_input(obj.get(Y_METADATA))
                if obj.get(Y_METADATA, None)
                else Metadata.from_name(obj.get(Y_NAME))
            )
            _spec = FabricStateSpec.from_input(obj.get(Y_SPEC, None))
            _status = FabricStateStatus.from_input(obj.get(Y_STATUS))
            return FabricState(
                metadata=_metadata,
                spec=_spec,
                status=_status,
            )
        return None  # pragma: no cover


class FabricStateList:
    def __init__(self, items: list[FabricState], listMeta: object | None = None):
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
    def from_input(obj) -> "FabricStateList | None":
        if obj:
            _items = obj.get(Y_ITEMS, [])
            _listMeta = obj.get(Y_METADATA, None)
            return FabricStateList(
                items=_items,
                listMeta=_listMeta,
            )
        return None  # pragma: no cover
