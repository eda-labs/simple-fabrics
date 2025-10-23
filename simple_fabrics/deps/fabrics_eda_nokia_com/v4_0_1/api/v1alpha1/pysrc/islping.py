#!/usr/bin/env python3
# Auto-generated classes based on your _types.go file (with special logic for CRDs that embed metav1.ObjectMeta)
# The change on this file will be overwritten by running edabuilder create or generate.
import eda_common as eda

from . import Y_NAME, Metadata
from .constants import *

ENUM_ISLPINGSTATUSRESULT_SUCCESS = "Success"
ENUM_ISLPINGSTATUSRESULT_FAILED = "Failed"
ENUM_ISLPINGSTATUSRESULT_PARTIALSUCCESS = "PartialSuccess"
Y_ISLS = "isls"
Y_ISLSELECTORS = "islSelectors"
Y_COUNT = "count"
Y_TIMEOUTSECONDS = "timeoutSeconds"
Y_RESULT = "result"
Y_DETAILS = "details"
# Package objects (GVK Schemas)
ISLPING_SCHEMA = eda.Schema(group="fabrics.eda.nokia.com", version="v1alpha1", kind="IslPing")


class IslPingSpec:
    def __init__(
        self,
        isls: list[str] | None = None,
        islSelectors: list[str] | None = None,
        count: int | None = None,
        timeoutSeconds: int | None = None,
    ):
        self.isls = isls
        self.islSelectors = islSelectors
        self.count = count
        self.timeoutSeconds = timeoutSeconds

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.isls is not None:
            _rval[Y_ISLS] = self.isls
        if self.islSelectors is not None:
            _rval[Y_ISLSELECTORS] = self.islSelectors
        if self.count is not None:
            _rval[Y_COUNT] = self.count
        if self.timeoutSeconds is not None:
            _rval[Y_TIMEOUTSECONDS] = self.timeoutSeconds
        return _rval

    @staticmethod
    def from_input(obj) -> "IslPingSpec | None":
        if obj:
            _isls = obj.get(Y_ISLS)
            _islSelectors = obj.get(Y_ISLSELECTORS)
            _count = obj.get(Y_COUNT, 1)
            _timeoutSeconds = obj.get(Y_TIMEOUTSECONDS, 5)
            return IslPingSpec(
                isls=_isls,
                islSelectors=_islSelectors,
                count=_count,
                timeoutSeconds=_timeoutSeconds,
            )
        return None  # pragma: no cover


class IslPingStatus:
    def __init__(
        self,
        result: object | None = None,
        details: list[object] | None = None,
    ):
        self.result = result
        self.details = details

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.result is not None:
            _rval[Y_RESULT] = self.result
        if self.details is not None:
            _rval[Y_DETAILS] = self.details
        return _rval

    @staticmethod
    def from_input(obj) -> "IslPingStatus | None":
        if obj:
            _result = obj.get(Y_RESULT)
            _details = obj.get(Y_DETAILS)
            return IslPingStatus(
                result=_result,
                details=_details,
            )
        return None  # pragma: no cover


class IslPing:
    def __init__(
        self, metadata: Metadata | None = None, spec: IslPingSpec | None = None, status: IslPingStatus | None = None
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
    def from_input(obj) -> "IslPing | None":
        if obj:
            _metadata = (
                Metadata.from_input(obj.get(Y_METADATA))
                if obj.get(Y_METADATA, None)
                else Metadata.from_name(obj.get(Y_NAME))
            )
            _spec = IslPingSpec.from_input(obj.get(Y_SPEC, None))
            _status = IslPingStatus.from_input(obj.get(Y_STATUS))
            return IslPing(
                metadata=_metadata,
                spec=_spec,
                status=_status,
            )
        return None  # pragma: no cover


class IslPingList:
    def __init__(self, items: list[IslPing], listMeta: object | None = None):
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
    def from_input(obj) -> "IslPingList | None":
        if obj:
            _items = obj.get(Y_ITEMS, [])
            _listMeta = obj.get(Y_METADATA, None)
            return IslPingList(
                items=_items,
                listMeta=_listMeta,
            )
        return None  # pragma: no cover
