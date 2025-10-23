#!/usr/bin/env python3
# Auto-generated classes based on your _types.go file (with special logic for CRDs that embed metav1.ObjectMeta)
# The change on this file will be overwritten by running edabuilder create or generate.
import eda_common as eda

from . import Y_NAME, Metadata
from .constants import *

Y_PROTOCOLS = "protocols"
Y_POOLIPV4ENABLED = "poolIPV4Enabled"
Y_POOLIPV6ENABLED = "poolIPV6Enabled"
Y_UNNUMBERED = "unnumbered"
Y_LOCALINTERFACE = "localInterface"
Y_REMOTEINTERFACE = "remoteInterface"
Y_DEFAULTINTERFACE = "defaultInterface"
Y_NODE = "node"
Y_IPV4ADDRESS = "IPv4Address"
Y_IPV6ADDRESS = "IPv6Address"
Y_BGPPEERIPV4 = "BGPPeerIPV4"
Y_BGPPEERIPV6 = "BGPPeerIPV6"
Y_DYNAMICBGPPEERIPV6 = "dynamicBGPPeerIPV6"
Y_OSPFV2 = "OSPFV2"
Y_OSPFV3 = "OSPFV3"
Y_OSPFINTERFACEIPV4 = "OSPFInterfaceIPV4"
Y_OSPFINTERFACEIPV6 = "OSPFInterfaceIPV6"
# Package objects (GVK Schemas)
ISLSTATE_SCHEMA = eda.Schema(group="fabrics.eda.nokia.com", version="v1alpha1", kind="ISLState")


class OSPFV2State:
    def __init__(
        self,
        OSPFInterfaceIPV4: str | None = None,
    ):
        self.OSPFInterfaceIPV4 = OSPFInterfaceIPV4

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.OSPFInterfaceIPV4 is not None:
            _rval[Y_OSPFINTERFACEIPV4] = self.OSPFInterfaceIPV4
        return _rval

    @staticmethod
    def from_input(obj) -> "OSPFV2State | None":
        if obj:
            _OSPFInterfaceIPV4 = obj.get(Y_OSPFINTERFACEIPV4)
            return OSPFV2State(
                OSPFInterfaceIPV4=_OSPFInterfaceIPV4,
            )
        return None  # pragma: no cover


class OSPFV3State:
    def __init__(
        self,
        OSPFInterfaceIPV4: str | None = None,
        OSPFInterfaceIPV6: str | None = None,
    ):
        self.OSPFInterfaceIPV4 = OSPFInterfaceIPV4
        self.OSPFInterfaceIPV6 = OSPFInterfaceIPV6

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.OSPFInterfaceIPV4 is not None:
            _rval[Y_OSPFINTERFACEIPV4] = self.OSPFInterfaceIPV4
        if self.OSPFInterfaceIPV6 is not None:
            _rval[Y_OSPFINTERFACEIPV6] = self.OSPFInterfaceIPV6
        return _rval

    @staticmethod
    def from_input(obj) -> "OSPFV3State | None":
        if obj:
            _OSPFInterfaceIPV4 = obj.get(Y_OSPFINTERFACEIPV4)
            _OSPFInterfaceIPV6 = obj.get(Y_OSPFINTERFACEIPV6)
            return OSPFV3State(
                OSPFInterfaceIPV4=_OSPFInterfaceIPV4,
                OSPFInterfaceIPV6=_OSPFInterfaceIPV6,
            )
        return None  # pragma: no cover


class LocalInterfaceState:
    def __init__(
        self,
        defaultInterface: str,
        node: str | None = None,
        IPv4Address: str | None = None,
        IPv6Address: str | None = None,
        BGPPeerIPV4: str | None = None,
        BGPPeerIPV6: str | None = None,
        dynamicBGPPeerIPV6: str | None = None,
        OSPFV2: OSPFV2State | None = None,
        OSPFV3: OSPFV3State | None = None,
    ):
        self.defaultInterface = defaultInterface
        self.node = node
        self.IPv4Address = IPv4Address
        self.IPv6Address = IPv6Address
        self.BGPPeerIPV4 = BGPPeerIPV4
        self.BGPPeerIPV6 = BGPPeerIPV6
        self.dynamicBGPPeerIPV6 = dynamicBGPPeerIPV6
        self.OSPFV2 = OSPFV2
        self.OSPFV3 = OSPFV3

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.defaultInterface is not None:
            _rval[Y_DEFAULTINTERFACE] = self.defaultInterface
        if self.node is not None:
            _rval[Y_NODE] = self.node
        if self.IPv4Address is not None:
            _rval[Y_IPV4ADDRESS] = self.IPv4Address
        if self.IPv6Address is not None:
            _rval[Y_IPV6ADDRESS] = self.IPv6Address
        if self.BGPPeerIPV4 is not None:
            _rval[Y_BGPPEERIPV4] = self.BGPPeerIPV4
        if self.BGPPeerIPV6 is not None:
            _rval[Y_BGPPEERIPV6] = self.BGPPeerIPV6
        if self.dynamicBGPPeerIPV6 is not None:
            _rval[Y_DYNAMICBGPPEERIPV6] = self.dynamicBGPPeerIPV6
        if self.OSPFV2 is not None:
            _rval[Y_OSPFV2] = self.OSPFV2.to_input()
        if self.OSPFV3 is not None:
            _rval[Y_OSPFV3] = self.OSPFV3.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> "LocalInterfaceState | None":
        if obj:
            _defaultInterface = obj.get(Y_DEFAULTINTERFACE)
            _node = obj.get(Y_NODE)
            _IPv4Address = obj.get(Y_IPV4ADDRESS)
            _IPv6Address = obj.get(Y_IPV6ADDRESS)
            _BGPPeerIPV4 = obj.get(Y_BGPPEERIPV4)
            _BGPPeerIPV6 = obj.get(Y_BGPPEERIPV6)
            _dynamicBGPPeerIPV6 = obj.get(Y_DYNAMICBGPPEERIPV6)
            _OSPFV2 = OSPFV2State.from_input(obj.get(Y_OSPFV2))
            _OSPFV3 = OSPFV3State.from_input(obj.get(Y_OSPFV3))
            return LocalInterfaceState(
                defaultInterface=_defaultInterface,
                node=_node,
                IPv4Address=_IPv4Address,
                IPv6Address=_IPv6Address,
                BGPPeerIPV4=_BGPPeerIPV4,
                BGPPeerIPV6=_BGPPeerIPV6,
                dynamicBGPPeerIPV6=_dynamicBGPPeerIPV6,
                OSPFV2=_OSPFV2,
                OSPFV3=_OSPFV3,
            )
        return None  # pragma: no cover


class RemoteInterfaceState:
    def __init__(
        self,
        defaultInterface: str,
        node: str | None = None,
        IPv4Address: str | None = None,
        IPv6Address: str | None = None,
        BGPPeerIPV4: str | None = None,
        BGPPeerIPV6: str | None = None,
        dynamicBGPPeerIPV6: str | None = None,
        OSPFV2: OSPFV2State | None = None,
        OSPFV3: OSPFV3State | None = None,
    ):
        self.defaultInterface = defaultInterface
        self.node = node
        self.IPv4Address = IPv4Address
        self.IPv6Address = IPv6Address
        self.BGPPeerIPV4 = BGPPeerIPV4
        self.BGPPeerIPV6 = BGPPeerIPV6
        self.dynamicBGPPeerIPV6 = dynamicBGPPeerIPV6
        self.OSPFV2 = OSPFV2
        self.OSPFV3 = OSPFV3

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.defaultInterface is not None:
            _rval[Y_DEFAULTINTERFACE] = self.defaultInterface
        if self.node is not None:
            _rval[Y_NODE] = self.node
        if self.IPv4Address is not None:
            _rval[Y_IPV4ADDRESS] = self.IPv4Address
        if self.IPv6Address is not None:
            _rval[Y_IPV6ADDRESS] = self.IPv6Address
        if self.BGPPeerIPV4 is not None:
            _rval[Y_BGPPEERIPV4] = self.BGPPeerIPV4
        if self.BGPPeerIPV6 is not None:
            _rval[Y_BGPPEERIPV6] = self.BGPPeerIPV6
        if self.dynamicBGPPeerIPV6 is not None:
            _rval[Y_DYNAMICBGPPEERIPV6] = self.dynamicBGPPeerIPV6
        if self.OSPFV2 is not None:
            _rval[Y_OSPFV2] = self.OSPFV2.to_input()
        if self.OSPFV3 is not None:
            _rval[Y_OSPFV3] = self.OSPFV3.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> "RemoteInterfaceState | None":
        if obj:
            _defaultInterface = obj.get(Y_DEFAULTINTERFACE)
            _node = obj.get(Y_NODE)
            _IPv4Address = obj.get(Y_IPV4ADDRESS)
            _IPv6Address = obj.get(Y_IPV6ADDRESS)
            _BGPPeerIPV4 = obj.get(Y_BGPPEERIPV4)
            _BGPPeerIPV6 = obj.get(Y_BGPPEERIPV6)
            _dynamicBGPPeerIPV6 = obj.get(Y_DYNAMICBGPPEERIPV6)
            _OSPFV2 = OSPFV2State.from_input(obj.get(Y_OSPFV2))
            _OSPFV3 = OSPFV3State.from_input(obj.get(Y_OSPFV3))
            return RemoteInterfaceState(
                defaultInterface=_defaultInterface,
                node=_node,
                IPv4Address=_IPv4Address,
                IPv6Address=_IPv6Address,
                BGPPeerIPV4=_BGPPeerIPV4,
                BGPPeerIPV6=_BGPPeerIPV6,
                dynamicBGPPeerIPV6=_dynamicBGPPeerIPV6,
                OSPFV2=_OSPFV2,
                OSPFV3=_OSPFV3,
            )
        return None  # pragma: no cover


class ISLStateSpec:
    def __init__(
        self,
        protocols: list[str],
        poolIPV4Enabled: bool,
        poolIPV6Enabled: bool,
        localInterface: LocalInterfaceState,
        remoteInterface: RemoteInterfaceState,
        unnumbered: str | None = None,
    ):
        self.protocols = protocols
        self.poolIPV4Enabled = poolIPV4Enabled
        self.poolIPV6Enabled = poolIPV6Enabled
        self.localInterface = localInterface
        self.remoteInterface = remoteInterface
        self.unnumbered = unnumbered

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.protocols is not None:
            _rval[Y_PROTOCOLS] = self.protocols
        if self.poolIPV4Enabled is not None:
            _rval[Y_POOLIPV4ENABLED] = self.poolIPV4Enabled
        if self.poolIPV6Enabled is not None:
            _rval[Y_POOLIPV6ENABLED] = self.poolIPV6Enabled
        if self.localInterface is not None:
            _rval[Y_LOCALINTERFACE] = self.localInterface.to_input()
        if self.remoteInterface is not None:
            _rval[Y_REMOTEINTERFACE] = self.remoteInterface.to_input()
        if self.unnumbered is not None:
            _rval[Y_UNNUMBERED] = self.unnumbered
        return _rval

    @staticmethod
    def from_input(obj) -> "ISLStateSpec | None":
        if obj:
            _protocols = obj.get(Y_PROTOCOLS)
            _poolIPV4Enabled = obj.get(Y_POOLIPV4ENABLED)
            _poolIPV6Enabled = obj.get(Y_POOLIPV6ENABLED)
            _localInterface = LocalInterfaceState.from_input(obj.get(Y_LOCALINTERFACE))
            _remoteInterface = RemoteInterfaceState.from_input(obj.get(Y_REMOTEINTERFACE))
            _unnumbered = obj.get(Y_UNNUMBERED)
            return ISLStateSpec(
                protocols=_protocols,
                poolIPV4Enabled=_poolIPV4Enabled,
                poolIPV6Enabled=_poolIPV6Enabled,
                localInterface=_localInterface,
                remoteInterface=_remoteInterface,
                unnumbered=_unnumbered,
            )
        return None  # pragma: no cover


class ISLStateStatus:
    def __init__(
        self,
    ):
        pass

    def to_input(self):  # pragma: no cover
        _rval = {}
        return _rval

    @staticmethod
    def from_input(obj) -> "ISLStateStatus | None":
        if obj:
            return ISLStateStatus()
        return None  # pragma: no cover


class ISLState:
    def __init__(
        self, metadata: Metadata | None = None, spec: ISLStateSpec | None = None, status: ISLStateStatus | None = None
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
    def from_input(obj) -> "ISLState | None":
        if obj:
            _metadata = (
                Metadata.from_input(obj.get(Y_METADATA))
                if obj.get(Y_METADATA, None)
                else Metadata.from_name(obj.get(Y_NAME))
            )
            _spec = ISLStateSpec.from_input(obj.get(Y_SPEC, None))
            _status = ISLStateStatus.from_input(obj.get(Y_STATUS))
            return ISLState(
                metadata=_metadata,
                spec=_spec,
                status=_status,
            )
        return None  # pragma: no cover


class ISLStateList:
    def __init__(self, items: list[ISLState], listMeta: object | None = None):
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
    def from_input(obj) -> "ISLStateList | None":
        if obj:
            _items = obj.get(Y_ITEMS, [])
            _listMeta = obj.get(Y_METADATA, None)
            return ISLStateList(
                items=_items,
                listMeta=_listMeta,
            )
        return None  # pragma: no cover
