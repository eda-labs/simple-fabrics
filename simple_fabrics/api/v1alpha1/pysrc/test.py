#!/usr/bin/env python3
# Auto-generated classes based on your _types.go file (with special logic for CRDs that embed metav1.ObjectMeta)
# The change on this file will be overwritten by running edabuilder create or generate.
import eda_common as eda

from . import Metadata, Y_NAME

from simple_fabrics.api.v1alpha1.pysrc.constants import *
Y_FOO = 'foo'
Y_BAZ = 'baz'
# Package objects (GVK Schemas)
TEST_SCHEMA = eda.Schema(group='simple-fabrics.eda.local', version='v1alpha1', kind='Test')


class TestSpec:
    def __init__(
        self,
        foo: str,
    ):
        self.foo = foo

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.foo is not None:
            _rval[Y_FOO] = self.foo
        return _rval

    @staticmethod
    def from_input(obj) -> 'TestSpec | None':
        if obj:
            _foo = obj.get(Y_FOO)
            return TestSpec(
                foo=_foo,
            )
        return None  # pragma: no cover


class TestStatus:
    def __init__(
        self,
        baz: str | None = None,
    ):
        self.baz = baz

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.baz is not None:
            _rval[Y_BAZ] = self.baz
        return _rval

    @staticmethod
    def from_input(obj) -> 'TestStatus | None':
        if obj:
            _baz = obj.get(Y_BAZ)
            return TestStatus(
                baz=_baz,
            )
        return None  # pragma: no cover


class Test:
    def __init__(
        self,
        metadata: Metadata | None = None,
        spec: TestSpec | None = None,
        status: TestStatus | None = None
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
    def from_input(obj) -> 'Test | None':
        if obj:
            _metadata = (
                Metadata.from_input(obj.get(Y_METADATA))
                if obj.get(Y_METADATA, None)
                else Metadata.from_name(obj.get(Y_NAME))
            )
            _spec = TestSpec.from_input(obj.get(Y_SPEC, None))
            _status = TestStatus.from_input(obj.get(Y_STATUS))
            return Test(
                metadata=_metadata,
                spec=_spec,
                status=_status,
            )
        return None  # pragma: no cover


class TestList:
    def __init__(
        self,
        items: list[Test],
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
    def from_input(obj) -> 'TestList | None':
        if obj:
            _items = obj.get(Y_ITEMS, [])
            _listMeta = obj.get(Y_METADATA, None)
            return TestList(
                items=_items,
                listMeta=_listMeta,
            )
        return None  # pragma: no cover
