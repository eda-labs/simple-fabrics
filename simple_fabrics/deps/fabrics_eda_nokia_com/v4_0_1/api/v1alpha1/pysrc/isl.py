#!/usr/bin/env python3
# Auto-generated classes based on your _types.go file (with special logic for CRDs that embed metav1.ObjectMeta)
# The change on this file will be overwritten by running edabuilder create or generate.
import eda_common as eda

from . import Y_NAME, Metadata
from .constants import *

ENUM_ISLSPECUNNUMBERED_IPV6 = "IPV6"
ENUM_ISLSPECUNNUMBERED_ = ""

ENUM_OSPFPROTOCOLENUMS_OSPFV2 = "OSPFv2"
ENUM_OSPFPROTOCOLENUMS_OSPFV3 = "OSPFv3"
Y_POOLIPV4 = "poolIPV4"
Y_POOLIPV6 = "poolIPV6"
Y_BFD = "bfd"
Y_IPMTU = "ipMTU"
Y_VLANID = "vlanID"
Y_BGP = "bgp"
Y_LOCALINTERFACE = "localInterface"
Y_REMOTEINTERFACE = "remoteInterface"
Y_LOCALDEFAULTROUTER = "localDefaultRouter"
Y_REMOTEDEFAULTROUTER = "remoteDefaultRouter"
Y_UNNUMBERED = "unnumbered"
Y_QOS = "qos"
Y_OSPF = "ospf"
Y_INGRESSPOLICY = "ingressPolicy"
Y_EGRESSPOLICY = "egressPolicy"
Y_ENABLED = "enabled"
Y_LOCALINTERFACEAS = "localInterfaceAS"
Y_REMOTEINTERFACEAS = "remoteInterfaceAS"
Y_AFISAFI = "afiSAFI"
Y_IMPORTPOLICY = "importPolicy"
Y_EXPORTPOLICY = "exportPolicy"
Y_BGPGROUP = "bgpGroup"
Y_KEYCHAIN = "keychain"
Y_OSPFV2 = "ospfv2"
Y_OSPFV3 = "ospfv3"
Y_LOCALIPV4INSTANCE = "localIPV4Instance"
Y_REMOTEIPV4INSTANCE = "remoteIPV4Instance"
Y_LOCALIPV4AREA = "localIPV4Area"
Y_REMOTEIPV4AREA = "remoteIPV4Area"
Y_LOCALIPV6INSTANCE = "localIPV6Instance"
Y_REMOTEIPV6INSTANCE = "remoteIPV6Instance"
Y_LOCALIPV6AREA = "localIPV6Area"
Y_REMOTEIPV6AREA = "remoteIPV6Area"
Y_DESIREDMINTRANSMITINT = "desiredMinTransmitInt"
Y_REQUIREDMINRECEIVE = "requiredMinReceive"
Y_DETECTIONMULTIPLIER = "detectionMultiplier"
Y_MINECHORECEIVEINTERVAL = "minEchoReceiveInterval"
Y_TTL = "ttl"
Y_HEALTH = "health"
Y_HEALTHSCOREREASON = "healthScoreReason"
Y_OPERATIONALSTATE = "operationalState"
Y_LASTCHANGE = "lastChange"
Y_DEFAULTINTERFACE = "defaultInterface"
Y_NODE = "node"
Y_IPV4ADDRESS = "IPv4Address"
Y_IPV6ADDRESS = "IPv6Address"
# Package objects (GVK Schemas)
ISL_SCHEMA = eda.Schema(group="fabrics.eda.nokia.com", version="v1alpha1", kind="ISL")


class BFD:
    def __init__(
        self,
        enabled: bool | None = None,
        desiredMinTransmitInt: int | None = None,
        requiredMinReceive: int | None = None,
        detectionMultiplier: int | None = None,
        minEchoReceiveInterval: int | None = None,
        ttl: int | None = None,
    ):
        self.enabled = enabled
        self.desiredMinTransmitInt = desiredMinTransmitInt
        self.requiredMinReceive = requiredMinReceive
        self.detectionMultiplier = detectionMultiplier
        self.minEchoReceiveInterval = minEchoReceiveInterval
        self.ttl = ttl

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.enabled is not None:
            _rval[Y_ENABLED] = self.enabled
        if self.desiredMinTransmitInt is not None:
            _rval[Y_DESIREDMINTRANSMITINT] = self.desiredMinTransmitInt
        if self.requiredMinReceive is not None:
            _rval[Y_REQUIREDMINRECEIVE] = self.requiredMinReceive
        if self.detectionMultiplier is not None:
            _rval[Y_DETECTIONMULTIPLIER] = self.detectionMultiplier
        if self.minEchoReceiveInterval is not None:
            _rval[Y_MINECHORECEIVEINTERVAL] = self.minEchoReceiveInterval
        if self.ttl is not None:
            _rval[Y_TTL] = self.ttl
        return _rval

    @staticmethod
    def from_input(obj) -> "BFD | None":
        if obj:
            _enabled = obj.get(Y_ENABLED, False)
            _desiredMinTransmitInt = obj.get(Y_DESIREDMINTRANSMITINT, 1000000)
            _requiredMinReceive = obj.get(Y_REQUIREDMINRECEIVE, 1000000)
            _detectionMultiplier = obj.get(Y_DETECTIONMULTIPLIER, 3)
            _minEchoReceiveInterval = obj.get(Y_MINECHORECEIVEINTERVAL, 1000000)
            _ttl = obj.get(Y_TTL)
            return BFD(
                enabled=_enabled,
                desiredMinTransmitInt=_desiredMinTransmitInt,
                requiredMinReceive=_requiredMinReceive,
                detectionMultiplier=_detectionMultiplier,
                minEchoReceiveInterval=_minEchoReceiveInterval,
                ttl=_ttl,
            )
        return None  # pragma: no cover


class BGP:
    def __init__(
        self,
        enabled: bool,
        localInterfaceAS: int,
        remoteInterfaceAS: int,
        afiSAFI: list[str] | None = None,
        importPolicy: list[str] | None = None,
        exportPolicy: list[str] | None = None,
        bgpGroup: str | None = None,
        keychain: str | None = None,
    ):
        self.enabled = enabled
        self.localInterfaceAS = localInterfaceAS
        self.remoteInterfaceAS = remoteInterfaceAS
        self.afiSAFI = afiSAFI
        self.importPolicy = importPolicy
        self.exportPolicy = exportPolicy
        self.bgpGroup = bgpGroup
        self.keychain = keychain

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.enabled is not None:
            _rval[Y_ENABLED] = self.enabled
        if self.localInterfaceAS is not None:
            _rval[Y_LOCALINTERFACEAS] = self.localInterfaceAS
        if self.remoteInterfaceAS is not None:
            _rval[Y_REMOTEINTERFACEAS] = self.remoteInterfaceAS
        if self.afiSAFI is not None:
            _rval[Y_AFISAFI] = self.afiSAFI
        if self.importPolicy is not None:
            _rval[Y_IMPORTPOLICY] = self.importPolicy
        if self.exportPolicy is not None:
            _rval[Y_EXPORTPOLICY] = self.exportPolicy
        if self.bgpGroup is not None:
            _rval[Y_BGPGROUP] = self.bgpGroup
        if self.keychain is not None:
            _rval[Y_KEYCHAIN] = self.keychain
        return _rval

    @staticmethod
    def from_input(obj) -> "BGP | None":
        if obj:
            _enabled = obj.get(Y_ENABLED, False)
            _localInterfaceAS = obj.get(Y_LOCALINTERFACEAS)
            _remoteInterfaceAS = obj.get(Y_REMOTEINTERFACEAS)
            _afiSAFI = obj.get(Y_AFISAFI)
            _importPolicy = obj.get(Y_IMPORTPOLICY)
            _exportPolicy = obj.get(Y_EXPORTPOLICY)
            _bgpGroup = obj.get(Y_BGPGROUP)
            _keychain = obj.get(Y_KEYCHAIN)
            return BGP(
                enabled=_enabled,
                localInterfaceAS=_localInterfaceAS,
                remoteInterfaceAS=_remoteInterfaceAS,
                afiSAFI=_afiSAFI,
                importPolicy=_importPolicy,
                exportPolicy=_exportPolicy,
                bgpGroup=_bgpGroup,
                keychain=_keychain,
            )
        return None  # pragma: no cover


class OSPFV2:
    def __init__(
        self,
        localIPV4Instance: str | None = None,
        remoteIPV4Instance: str | None = None,
        localIPV4Area: str | None = None,
        remoteIPV4Area: str | None = None,
    ):
        self.localIPV4Instance = localIPV4Instance
        self.remoteIPV4Instance = remoteIPV4Instance
        self.localIPV4Area = localIPV4Area
        self.remoteIPV4Area = remoteIPV4Area

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.localIPV4Instance is not None:
            _rval[Y_LOCALIPV4INSTANCE] = self.localIPV4Instance
        if self.remoteIPV4Instance is not None:
            _rval[Y_REMOTEIPV4INSTANCE] = self.remoteIPV4Instance
        if self.localIPV4Area is not None:
            _rval[Y_LOCALIPV4AREA] = self.localIPV4Area
        if self.remoteIPV4Area is not None:
            _rval[Y_REMOTEIPV4AREA] = self.remoteIPV4Area
        return _rval

    @staticmethod
    def from_input(obj) -> "OSPFV2 | None":
        if obj:
            _localIPV4Instance = obj.get(Y_LOCALIPV4INSTANCE)
            _remoteIPV4Instance = obj.get(Y_REMOTEIPV4INSTANCE)
            _localIPV4Area = obj.get(Y_LOCALIPV4AREA)
            _remoteIPV4Area = obj.get(Y_REMOTEIPV4AREA)
            return OSPFV2(
                localIPV4Instance=_localIPV4Instance,
                remoteIPV4Instance=_remoteIPV4Instance,
                localIPV4Area=_localIPV4Area,
                remoteIPV4Area=_remoteIPV4Area,
            )
        return None  # pragma: no cover


class OSPFV3:
    def __init__(
        self,
        localIPV4Instance: str | None = None,
        remoteIPV4Instance: str | None = None,
        localIPV6Instance: str | None = None,
        remoteIPV6Instance: str | None = None,
        localIPV4Area: str | None = None,
        localIPV6Area: str | None = None,
        remoteIPV4Area: str | None = None,
        remoteIPV6Area: str | None = None,
    ):
        self.localIPV4Instance = localIPV4Instance
        self.remoteIPV4Instance = remoteIPV4Instance
        self.localIPV6Instance = localIPV6Instance
        self.remoteIPV6Instance = remoteIPV6Instance
        self.localIPV4Area = localIPV4Area
        self.localIPV6Area = localIPV6Area
        self.remoteIPV4Area = remoteIPV4Area
        self.remoteIPV6Area = remoteIPV6Area

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.localIPV4Instance is not None:
            _rval[Y_LOCALIPV4INSTANCE] = self.localIPV4Instance
        if self.remoteIPV4Instance is not None:
            _rval[Y_REMOTEIPV4INSTANCE] = self.remoteIPV4Instance
        if self.localIPV6Instance is not None:
            _rval[Y_LOCALIPV6INSTANCE] = self.localIPV6Instance
        if self.remoteIPV6Instance is not None:
            _rval[Y_REMOTEIPV6INSTANCE] = self.remoteIPV6Instance
        if self.localIPV4Area is not None:
            _rval[Y_LOCALIPV4AREA] = self.localIPV4Area
        if self.localIPV6Area is not None:
            _rval[Y_LOCALIPV6AREA] = self.localIPV6Area
        if self.remoteIPV4Area is not None:
            _rval[Y_REMOTEIPV4AREA] = self.remoteIPV4Area
        if self.remoteIPV6Area is not None:
            _rval[Y_REMOTEIPV6AREA] = self.remoteIPV6Area
        return _rval

    @staticmethod
    def from_input(obj) -> "OSPFV3 | None":
        if obj:
            _localIPV4Instance = obj.get(Y_LOCALIPV4INSTANCE)
            _remoteIPV4Instance = obj.get(Y_REMOTEIPV4INSTANCE)
            _localIPV6Instance = obj.get(Y_LOCALIPV6INSTANCE)
            _remoteIPV6Instance = obj.get(Y_REMOTEIPV6INSTANCE)
            _localIPV4Area = obj.get(Y_LOCALIPV4AREA)
            _localIPV6Area = obj.get(Y_LOCALIPV6AREA)
            _remoteIPV4Area = obj.get(Y_REMOTEIPV4AREA)
            _remoteIPV6Area = obj.get(Y_REMOTEIPV6AREA)
            return OSPFV3(
                localIPV4Instance=_localIPV4Instance,
                remoteIPV4Instance=_remoteIPV4Instance,
                localIPV6Instance=_localIPV6Instance,
                remoteIPV6Instance=_remoteIPV6Instance,
                localIPV4Area=_localIPV4Area,
                localIPV6Area=_localIPV6Area,
                remoteIPV4Area=_remoteIPV4Area,
                remoteIPV6Area=_remoteIPV6Area,
            )
        return None  # pragma: no cover


class OSPF:
    def __init__(
        self,
        enabled: bool,
        ospfv2: OSPFV2 | None = None,
        ospfv3: OSPFV3 | None = None,
    ):
        self.enabled = enabled
        self.ospfv2 = ospfv2
        self.ospfv3 = ospfv3

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.enabled is not None:
            _rval[Y_ENABLED] = self.enabled
        if self.ospfv2 is not None:
            _rval[Y_OSPFV2] = self.ospfv2.to_input()
        if self.ospfv3 is not None:
            _rval[Y_OSPFV3] = self.ospfv3.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> "OSPF | None":
        if obj:
            _enabled = obj.get(Y_ENABLED)
            _ospfv2 = OSPFV2.from_input(obj.get(Y_OSPFV2))
            _ospfv3 = OSPFV3.from_input(obj.get(Y_OSPFV3))
            return OSPF(
                enabled=_enabled,
                ospfv2=_ospfv2,
                ospfv3=_ospfv3,
            )
        return None  # pragma: no cover


class QoS:
    def __init__(
        self,
        ingressPolicy: str | None = None,
        egressPolicy: str | None = None,
    ):
        self.ingressPolicy = ingressPolicy
        self.egressPolicy = egressPolicy

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.ingressPolicy is not None:
            _rval[Y_INGRESSPOLICY] = self.ingressPolicy
        if self.egressPolicy is not None:
            _rval[Y_EGRESSPOLICY] = self.egressPolicy
        return _rval

    @staticmethod
    def from_input(obj) -> "QoS | None":
        if obj:
            _ingressPolicy = obj.get(Y_INGRESSPOLICY)
            _egressPolicy = obj.get(Y_EGRESSPOLICY)
            return QoS(
                ingressPolicy=_ingressPolicy,
                egressPolicy=_egressPolicy,
            )
        return None  # pragma: no cover


class ISLSpec:
    def __init__(
        self,
        localInterface: str,
        remoteInterface: str,
        localDefaultRouter: str,
        remoteDefaultRouter: str,
        poolIPV4: str | None = None,
        poolIPV6: str | None = None,
        bfd: BFD | None = None,
        ipMTU: int | None = None,
        vlanID: int | None = None,
        bgp: BGP | None = None,
        unnumbered: str | None = None,
        qos: QoS | None = None,
        ospf: OSPF | None = None,
    ):
        self.localInterface = localInterface
        self.remoteInterface = remoteInterface
        self.localDefaultRouter = localDefaultRouter
        self.remoteDefaultRouter = remoteDefaultRouter
        self.poolIPV4 = poolIPV4
        self.poolIPV6 = poolIPV6
        self.bfd = bfd
        self.ipMTU = ipMTU
        self.vlanID = vlanID
        self.bgp = bgp
        self.unnumbered = unnumbered
        self.qos = qos
        self.ospf = ospf

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.localInterface is not None:
            _rval[Y_LOCALINTERFACE] = self.localInterface
        if self.remoteInterface is not None:
            _rval[Y_REMOTEINTERFACE] = self.remoteInterface
        if self.localDefaultRouter is not None:
            _rval[Y_LOCALDEFAULTROUTER] = self.localDefaultRouter
        if self.remoteDefaultRouter is not None:
            _rval[Y_REMOTEDEFAULTROUTER] = self.remoteDefaultRouter
        if self.poolIPV4 is not None:
            _rval[Y_POOLIPV4] = self.poolIPV4
        if self.poolIPV6 is not None:
            _rval[Y_POOLIPV6] = self.poolIPV6
        if self.bfd is not None:
            _rval[Y_BFD] = self.bfd.to_input()
        if self.ipMTU is not None:
            _rval[Y_IPMTU] = self.ipMTU
        if self.vlanID is not None:
            _rval[Y_VLANID] = self.vlanID
        if self.bgp is not None:
            _rval[Y_BGP] = self.bgp.to_input()
        if self.unnumbered is not None:
            _rval[Y_UNNUMBERED] = self.unnumbered
        if self.qos is not None:
            _rval[Y_QOS] = self.qos.to_input()
        if self.ospf is not None:
            _rval[Y_OSPF] = self.ospf.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> "ISLSpec | None":
        if obj:
            _localInterface = obj.get(Y_LOCALINTERFACE)
            _remoteInterface = obj.get(Y_REMOTEINTERFACE)
            _localDefaultRouter = obj.get(Y_LOCALDEFAULTROUTER)
            _remoteDefaultRouter = obj.get(Y_REMOTEDEFAULTROUTER)
            _poolIPV4 = obj.get(Y_POOLIPV4)
            _poolIPV6 = obj.get(Y_POOLIPV6)
            _bfd = BFD.from_input(obj.get(Y_BFD))
            _ipMTU = obj.get(Y_IPMTU)
            _vlanID = obj.get(Y_VLANID)
            _bgp = BGP.from_input(obj.get(Y_BGP))
            _unnumbered = obj.get(Y_UNNUMBERED)
            _qos = QoS.from_input(obj.get(Y_QOS))
            _ospf = OSPF.from_input(obj.get(Y_OSPF))
            return ISLSpec(
                localInterface=_localInterface,
                remoteInterface=_remoteInterface,
                localDefaultRouter=_localDefaultRouter,
                remoteDefaultRouter=_remoteDefaultRouter,
                poolIPV4=_poolIPV4,
                poolIPV6=_poolIPV6,
                bfd=_bfd,
                ipMTU=_ipMTU,
                vlanID=_vlanID,
                bgp=_bgp,
                unnumbered=_unnumbered,
                qos=_qos,
                ospf=_ospf,
            )
        return None  # pragma: no cover


class LocalInterface:
    def __init__(
        self,
        defaultInterface: str | None = None,
        node: str | None = None,
        IPv4Address: str | None = None,
        IPv6Address: str | None = None,
    ):
        self.defaultInterface = defaultInterface
        self.node = node
        self.IPv4Address = IPv4Address
        self.IPv6Address = IPv6Address

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
        return _rval

    @staticmethod
    def from_input(obj) -> "LocalInterface | None":
        if obj:
            _defaultInterface = obj.get(Y_DEFAULTINTERFACE)
            _node = obj.get(Y_NODE)
            _IPv4Address = obj.get(Y_IPV4ADDRESS)
            _IPv6Address = obj.get(Y_IPV6ADDRESS)
            return LocalInterface(
                defaultInterface=_defaultInterface,
                node=_node,
                IPv4Address=_IPv4Address,
                IPv6Address=_IPv6Address,
            )
        return None  # pragma: no cover


class RemoteInterface:
    def __init__(
        self,
        defaultInterface: str | None = None,
        node: str | None = None,
        IPv4Address: str | None = None,
        IPv6Address: str | None = None,
    ):
        self.defaultInterface = defaultInterface
        self.node = node
        self.IPv4Address = IPv4Address
        self.IPv6Address = IPv6Address

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
        return _rval

    @staticmethod
    def from_input(obj) -> "RemoteInterface | None":
        if obj:
            _defaultInterface = obj.get(Y_DEFAULTINTERFACE)
            _node = obj.get(Y_NODE)
            _IPv4Address = obj.get(Y_IPV4ADDRESS)
            _IPv6Address = obj.get(Y_IPV6ADDRESS)
            return RemoteInterface(
                defaultInterface=_defaultInterface,
                node=_node,
                IPv4Address=_IPv4Address,
                IPv6Address=_IPv6Address,
            )
        return None  # pragma: no cover


class ISLStatus:
    def __init__(
        self,
        health: int | None = None,
        healthScoreReason: str | None = None,
        operationalState: str | None = None,
        lastChange: str | None = None,
        localInterface: LocalInterface | None = None,
        remoteInterface: RemoteInterface | None = None,
    ):
        self.health = health
        self.healthScoreReason = healthScoreReason
        self.operationalState = operationalState
        self.lastChange = lastChange
        self.localInterface = localInterface
        self.remoteInterface = remoteInterface

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.health is not None:
            _rval[Y_HEALTH] = self.health
        if self.healthScoreReason is not None:
            _rval[Y_HEALTHSCOREREASON] = self.healthScoreReason
        if self.operationalState is not None:
            _rval[Y_OPERATIONALSTATE] = self.operationalState
        if self.lastChange is not None:
            _rval[Y_LASTCHANGE] = self.lastChange
        if self.localInterface is not None:
            _rval[Y_LOCALINTERFACE] = self.localInterface.to_input()
        if self.remoteInterface is not None:
            _rval[Y_REMOTEINTERFACE] = self.remoteInterface.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> "ISLStatus | None":
        if obj:
            _health = obj.get(Y_HEALTH)
            _healthScoreReason = obj.get(Y_HEALTHSCOREREASON)
            _operationalState = obj.get(Y_OPERATIONALSTATE)
            _lastChange = obj.get(Y_LASTCHANGE)
            _localInterface = LocalInterface.from_input(obj.get(Y_LOCALINTERFACE))
            _remoteInterface = RemoteInterface.from_input(obj.get(Y_REMOTEINTERFACE))
            return ISLStatus(
                health=_health,
                healthScoreReason=_healthScoreReason,
                operationalState=_operationalState,
                lastChange=_lastChange,
                localInterface=_localInterface,
                remoteInterface=_remoteInterface,
            )
        return None  # pragma: no cover


class ISL:
    def __init__(self, metadata: Metadata | None = None, spec: ISLSpec | None = None, status: ISLStatus | None = None):
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
    def from_input(obj) -> "ISL | None":
        if obj:
            _metadata = (
                Metadata.from_input(obj.get(Y_METADATA))
                if obj.get(Y_METADATA, None)
                else Metadata.from_name(obj.get(Y_NAME))
            )
            _spec = ISLSpec.from_input(obj.get(Y_SPEC, None))
            _status = ISLStatus.from_input(obj.get(Y_STATUS))
            return ISL(
                metadata=_metadata,
                spec=_spec,
                status=_status,
            )
        return None  # pragma: no cover


class ISLList:
    def __init__(self, items: list[ISL], listMeta: object | None = None):
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
    def from_input(obj) -> "ISLList | None":
        if obj:
            _items = obj.get(Y_ITEMS, [])
            _listMeta = obj.get(Y_METADATA, None)
            return ISLList(
                items=_items,
                listMeta=_listMeta,
            )
        return None  # pragma: no cover
