#!/usr/bin/env python3
# Auto-generated classes based on your _types.go file (with special logic for CRDs that embed metav1.ObjectMeta)
# The change on this file will be overwritten by running edabuilder create or generate.
import eda_common as eda

from . import Y_NAME, Metadata

# from fabrics.api.v1alpha1.pysrc.constants import *
# from fabrics.api.v1alpha1.pysrc.isl import BFD, QoS
from .constants import *
from .isl import BFD, QoS

ENUM_INTERSWITCHLINKSUNNUMBERED_IPV6 = "IPV6"
ENUM_INTERSWITCHLINKSUNNUMBERED_ = ""

ENUM_OSPFADDRESSFAMILIES_IPV4_UNICAST = "IPV4-UNICAST"
ENUM_OSPFADDRESSFAMILIES_IPV6_UNICAST = "IPV6-UNICAST"

ENUM_UNDERLAYPROTOCOLENUMS_EBGP = "EBGP"
ENUM_UNDERLAYPROTOCOLENUMS_OSPFV2 = "OSPFv2"
ENUM_UNDERLAYPROTOCOLENUMS_OSPFV3 = "OSPFv3"

ENUM_OVERLAYPROTOCOLPROTOCOL_IBGP = "IBGP"
ENUM_OVERLAYPROTOCOLPROTOCOL_EBGP = "EBGP"
ENUM_OVERLAYPROTOCOLPROTOCOL_ = ""
Y_SYSTEMPOOLIPV4 = "systemPoolIPV4"
Y_SYSTEMPOOLIPV6 = "systemPoolIPV6"
Y_LEAFS = "leafs"
Y_SPINES = "spines"
Y_SUPERSPINES = "superSpines"
Y_BORDERLEAFS = "borderLeafs"
Y_INTERSWITCHLINKS = "interSwitchLinks"
Y_UNDERLAYPROTOCOL = "underlayProtocol"
Y_OVERLAYPROTOCOL = "overlayProtocol"
Y_FABRICSELECTOR = "fabricSelector"
Y_ROUTELEAKING = "routeLeaking"
Y_IMPORTPOLICY = "importPolicy"
Y_EXPORTPOLICY = "exportPolicy"
Y_LINKSELECTOR = "linkSelector"
Y_POOLIPV4 = "poolIPV4"
Y_POOLIPV6 = "poolIPV6"
Y_VLANID = "vlanID"
Y_UNNUMBERED = "unnumbered"
Y_QOS = "qos"
Y_IPMTU = "ipMTU"
Y_LEAFNODESELECTOR = "leafNodeSelector"
Y_ASNPOOL = "asnPool"
Y_SPINENODESELECTOR = "spineNodeSelector"
Y_SUPERSPINENODESELECTOR = "superSpineNodeSelector"
Y_BORDERLEAFNODESELECTOR = "borderLeafNodeSelector"
Y_PROTOCOL = "protocol"
Y_BFD = "bfd"
Y_BGP = "bgp"
Y_OSPF = "ospf"
Y_ADDRESSFAMILY = "addressFamily"
Y_TIMERS = "timers"
Y_KEYCHAIN = "keychain"
Y_AUTONOMOUSSYSTEM = "autonomousSystem"
Y_CLUSTERID = "clusterID"
Y_RRNODESELECTOR = "rrNodeSelector"
Y_RRIPADDRESSES = "rrIPAddresses"
Y_RRCLIENTNODESELECTOR = "rrClientNodeSelector"
Y_HOLDTIME = "holdTime"
Y_KEEPALIVE = "keepAlive"
Y_CONNECTRETRY = "connectRetry"
Y_MINIMUMADVERTISEMENTINTERVAL = "minimumAdvertisementInterval"
Y_HEALTH = "health"
Y_HEALTHSCOREREASON = "healthScoreReason"
Y_OPERATIONALSTATE = "operationalState"
Y_LASTCHANGE = "lastChange"
Y_LEAFNODES = "leafNodes"
Y_BORDERLEAFNODES = "borderLeafNodes"
Y_SPINENODES = "spineNodes"
Y_SUPERSPINENODES = "superSpineNodes"
Y_NODE = "node"
Y_OPERATINGSYSTEM = "operatingSystem"
Y_OPERATINGSYSTEMVERSION = "operatingSystemVersion"
Y_UNDERLAYAUTONOMOUSSYSTEM = "underlayAutonomousSystem"
# Package objects (GVK Schemas)
FABRIC_SCHEMA = eda.Schema(group="fabrics.eda.nokia.com", version="v1alpha1", kind="Fabric")


class RouteLeaking:
    def __init__(
        self,
        importPolicy: str,
        exportPolicy: str,
    ):
        self.importPolicy = importPolicy
        self.exportPolicy = exportPolicy

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.importPolicy is not None:
            _rval[Y_IMPORTPOLICY] = self.importPolicy
        if self.exportPolicy is not None:
            _rval[Y_EXPORTPOLICY] = self.exportPolicy
        return _rval

    @staticmethod
    def from_input(obj) -> "RouteLeaking | None":
        if obj:
            _importPolicy = obj.get(Y_IMPORTPOLICY)
            _exportPolicy = obj.get(Y_EXPORTPOLICY)
            return RouteLeaking(
                importPolicy=_importPolicy,
                exportPolicy=_exportPolicy,
            )
        return None  # pragma: no cover


class BorderLeafs:
    def __init__(
        self,
        borderLeafNodeSelector: list[str] | None = None,
        systemPoolIPV4: str | None = None,
        systemPoolIPV6: str | None = None,
        asnPool: str | None = None,
        routeLeaking: RouteLeaking | None = None,
    ):
        self.borderLeafNodeSelector = borderLeafNodeSelector
        self.systemPoolIPV4 = systemPoolIPV4
        self.systemPoolIPV6 = systemPoolIPV6
        self.asnPool = asnPool
        self.routeLeaking = routeLeaking

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.borderLeafNodeSelector is not None:
            _rval[Y_BORDERLEAFNODESELECTOR] = self.borderLeafNodeSelector
        if self.systemPoolIPV4 is not None:
            _rval[Y_SYSTEMPOOLIPV4] = self.systemPoolIPV4
        if self.systemPoolIPV6 is not None:
            _rval[Y_SYSTEMPOOLIPV6] = self.systemPoolIPV6
        if self.asnPool is not None:
            _rval[Y_ASNPOOL] = self.asnPool
        if self.routeLeaking is not None:
            _rval[Y_ROUTELEAKING] = self.routeLeaking.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> "BorderLeafs | None":
        if obj:
            _borderLeafNodeSelector = obj.get(Y_BORDERLEAFNODESELECTOR)
            _systemPoolIPV4 = obj.get(Y_SYSTEMPOOLIPV4)
            _systemPoolIPV6 = obj.get(Y_SYSTEMPOOLIPV6)
            _asnPool = obj.get(Y_ASNPOOL)
            _routeLeaking = RouteLeaking.from_input(obj.get(Y_ROUTELEAKING))
            return BorderLeafs(
                borderLeafNodeSelector=_borderLeafNodeSelector,
                systemPoolIPV4=_systemPoolIPV4,
                systemPoolIPV6=_systemPoolIPV6,
                asnPool=_asnPool,
                routeLeaking=_routeLeaking,
            )
        return None  # pragma: no cover


class InterSwitchLinks:
    def __init__(
        self,
        linkSelector: list[str] | None = None,
        poolIPV4: str | None = None,
        poolIPV6: str | None = None,
        vlanID: int | None = None,
        unnumbered: str | None = None,
        qos: QoS | None = None,
        ipMTU: int | None = None,
    ):
        self.linkSelector = linkSelector
        self.poolIPV4 = poolIPV4
        self.poolIPV6 = poolIPV6
        self.vlanID = vlanID
        self.unnumbered = unnumbered
        self.qos = qos
        self.ipMTU = ipMTU

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.linkSelector is not None:
            _rval[Y_LINKSELECTOR] = self.linkSelector
        if self.poolIPV4 is not None:
            _rval[Y_POOLIPV4] = self.poolIPV4
        if self.poolIPV6 is not None:
            _rval[Y_POOLIPV6] = self.poolIPV6
        if self.vlanID is not None:
            _rval[Y_VLANID] = self.vlanID
        if self.unnumbered is not None:
            _rval[Y_UNNUMBERED] = self.unnumbered
        if self.qos is not None:
            _rval[Y_QOS] = self.qos.to_input()
        if self.ipMTU is not None:
            _rval[Y_IPMTU] = self.ipMTU
        return _rval

    @staticmethod
    def from_input(obj) -> "InterSwitchLinks | None":
        if obj:
            _linkSelector = obj.get(Y_LINKSELECTOR)
            _poolIPV4 = obj.get(Y_POOLIPV4)
            _poolIPV6 = obj.get(Y_POOLIPV6)
            _vlanID = obj.get(Y_VLANID)
            _unnumbered = obj.get(Y_UNNUMBERED)
            _qos = QoS.from_input(obj.get(Y_QOS))
            _ipMTU = obj.get(Y_IPMTU)
            return InterSwitchLinks(
                linkSelector=_linkSelector,
                poolIPV4=_poolIPV4,
                poolIPV6=_poolIPV6,
                vlanID=_vlanID,
                unnumbered=_unnumbered,
                qos=_qos,
                ipMTU=_ipMTU,
            )
        return None  # pragma: no cover


class Leafs:
    def __init__(
        self,
        leafNodeSelector: list[str] | None = None,
        systemPoolIPV4: str | None = None,
        systemPoolIPV6: str | None = None,
        asnPool: str | None = None,
        routeLeaking: RouteLeaking | None = None,
    ):
        self.leafNodeSelector = leafNodeSelector
        self.systemPoolIPV4 = systemPoolIPV4
        self.systemPoolIPV6 = systemPoolIPV6
        self.asnPool = asnPool
        self.routeLeaking = routeLeaking

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.leafNodeSelector is not None:
            _rval[Y_LEAFNODESELECTOR] = self.leafNodeSelector
        if self.systemPoolIPV4 is not None:
            _rval[Y_SYSTEMPOOLIPV4] = self.systemPoolIPV4
        if self.systemPoolIPV6 is not None:
            _rval[Y_SYSTEMPOOLIPV6] = self.systemPoolIPV6
        if self.asnPool is not None:
            _rval[Y_ASNPOOL] = self.asnPool
        if self.routeLeaking is not None:
            _rval[Y_ROUTELEAKING] = self.routeLeaking.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> "Leafs | None":
        if obj:
            _leafNodeSelector = obj.get(Y_LEAFNODESELECTOR)
            _systemPoolIPV4 = obj.get(Y_SYSTEMPOOLIPV4)
            _systemPoolIPV6 = obj.get(Y_SYSTEMPOOLIPV6)
            _asnPool = obj.get(Y_ASNPOOL)
            _routeLeaking = RouteLeaking.from_input(obj.get(Y_ROUTELEAKING))
            return Leafs(
                leafNodeSelector=_leafNodeSelector,
                systemPoolIPV4=_systemPoolIPV4,
                systemPoolIPV6=_systemPoolIPV6,
                asnPool=_asnPool,
                routeLeaking=_routeLeaking,
            )
        return None  # pragma: no cover


class Timers:
    def __init__(
        self,
        holdTime: int | None = None,
        keepAlive: int | None = None,
        connectRetry: int | None = None,
        minimumAdvertisementInterval: int | None = None,
    ):
        self.holdTime = holdTime
        self.keepAlive = keepAlive
        self.connectRetry = connectRetry
        self.minimumAdvertisementInterval = minimumAdvertisementInterval

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.holdTime is not None:
            _rval[Y_HOLDTIME] = self.holdTime
        if self.keepAlive is not None:
            _rval[Y_KEEPALIVE] = self.keepAlive
        if self.connectRetry is not None:
            _rval[Y_CONNECTRETRY] = self.connectRetry
        if self.minimumAdvertisementInterval is not None:
            _rval[Y_MINIMUMADVERTISEMENTINTERVAL] = self.minimumAdvertisementInterval
        return _rval

    @staticmethod
    def from_input(obj) -> "Timers | None":
        if obj:
            _holdTime = obj.get(Y_HOLDTIME)
            _keepAlive = obj.get(Y_KEEPALIVE)
            _connectRetry = obj.get(Y_CONNECTRETRY)
            _minimumAdvertisementInterval = obj.get(Y_MINIMUMADVERTISEMENTINTERVAL)
            return Timers(
                holdTime=_holdTime,
                keepAlive=_keepAlive,
                connectRetry=_connectRetry,
                minimumAdvertisementInterval=_minimumAdvertisementInterval,
            )
        return None  # pragma: no cover


class OverlayBGP:
    def __init__(
        self,
        exportPolicy: list[str] | None = None,
        importPolicy: list[str] | None = None,
        autonomousSystem: int | None = None,
        clusterID: str | None = None,
        rrNodeSelector: list[str] | None = None,
        rrIPAddresses: list[str] | None = None,
        rrClientNodeSelector: list[str] | None = None,
        timers: Timers | None = None,
        keychain: str | None = None,
    ):
        self.exportPolicy = exportPolicy
        self.importPolicy = importPolicy
        self.autonomousSystem = autonomousSystem
        self.clusterID = clusterID
        self.rrNodeSelector = rrNodeSelector
        self.rrIPAddresses = rrIPAddresses
        self.rrClientNodeSelector = rrClientNodeSelector
        self.timers = timers
        self.keychain = keychain

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.exportPolicy is not None:
            _rval[Y_EXPORTPOLICY] = self.exportPolicy
        if self.importPolicy is not None:
            _rval[Y_IMPORTPOLICY] = self.importPolicy
        if self.autonomousSystem is not None:
            _rval[Y_AUTONOMOUSSYSTEM] = self.autonomousSystem
        if self.clusterID is not None:
            _rval[Y_CLUSTERID] = self.clusterID
        if self.rrNodeSelector is not None:
            _rval[Y_RRNODESELECTOR] = self.rrNodeSelector
        if self.rrIPAddresses is not None:
            _rval[Y_RRIPADDRESSES] = self.rrIPAddresses
        if self.rrClientNodeSelector is not None:
            _rval[Y_RRCLIENTNODESELECTOR] = self.rrClientNodeSelector
        if self.timers is not None:
            _rval[Y_TIMERS] = self.timers.to_input()
        if self.keychain is not None:
            _rval[Y_KEYCHAIN] = self.keychain
        return _rval

    @staticmethod
    def from_input(obj) -> "OverlayBGP | None":
        if obj:
            _exportPolicy = obj.get(Y_EXPORTPOLICY)
            _importPolicy = obj.get(Y_IMPORTPOLICY)
            _autonomousSystem = obj.get(Y_AUTONOMOUSSYSTEM)
            _clusterID = obj.get(Y_CLUSTERID)
            _rrNodeSelector = obj.get(Y_RRNODESELECTOR)
            _rrIPAddresses = obj.get(Y_RRIPADDRESSES)
            _rrClientNodeSelector = obj.get(Y_RRCLIENTNODESELECTOR)
            _timers = Timers.from_input(obj.get(Y_TIMERS))
            _keychain = obj.get(Y_KEYCHAIN)
            return OverlayBGP(
                exportPolicy=_exportPolicy,
                importPolicy=_importPolicy,
                autonomousSystem=_autonomousSystem,
                clusterID=_clusterID,
                rrNodeSelector=_rrNodeSelector,
                rrIPAddresses=_rrIPAddresses,
                rrClientNodeSelector=_rrClientNodeSelector,
                timers=_timers,
                keychain=_keychain,
            )
        return None  # pragma: no cover


class OverlayProtocol:
    def __init__(
        self,
        protocol: str,
        bgp: OverlayBGP | None = None,
        bfd: BFD | None = None,
    ):
        self.protocol = protocol
        self.bgp = bgp
        self.bfd = bfd

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.protocol is not None:
            _rval[Y_PROTOCOL] = self.protocol
        if self.bgp is not None:
            _rval[Y_BGP] = self.bgp.to_input()
        if self.bfd is not None:
            _rval[Y_BFD] = self.bfd.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> "OverlayProtocol | None":
        if obj:
            _protocol = obj.get(Y_PROTOCOL)
            _bgp = OverlayBGP.from_input(obj.get(Y_BGP))
            _bfd = BFD.from_input(obj.get(Y_BFD))
            return OverlayProtocol(
                protocol=_protocol,
                bgp=_bgp,
                bfd=_bfd,
            )
        return None  # pragma: no cover


class Spines:
    def __init__(
        self,
        spineNodeSelector: list[str] | None = None,
        systemPoolIPV4: str | None = None,
        systemPoolIPV6: str | None = None,
        asnPool: str | None = None,
        routeLeaking: RouteLeaking | None = None,
    ):
        self.spineNodeSelector = spineNodeSelector
        self.systemPoolIPV4 = systemPoolIPV4
        self.systemPoolIPV6 = systemPoolIPV6
        self.asnPool = asnPool
        self.routeLeaking = routeLeaking

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.spineNodeSelector is not None:
            _rval[Y_SPINENODESELECTOR] = self.spineNodeSelector
        if self.systemPoolIPV4 is not None:
            _rval[Y_SYSTEMPOOLIPV4] = self.systemPoolIPV4
        if self.systemPoolIPV6 is not None:
            _rval[Y_SYSTEMPOOLIPV6] = self.systemPoolIPV6
        if self.asnPool is not None:
            _rval[Y_ASNPOOL] = self.asnPool
        if self.routeLeaking is not None:
            _rval[Y_ROUTELEAKING] = self.routeLeaking.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> "Spines | None":
        if obj:
            _spineNodeSelector = obj.get(Y_SPINENODESELECTOR)
            _systemPoolIPV4 = obj.get(Y_SYSTEMPOOLIPV4)
            _systemPoolIPV6 = obj.get(Y_SYSTEMPOOLIPV6)
            _asnPool = obj.get(Y_ASNPOOL)
            _routeLeaking = RouteLeaking.from_input(obj.get(Y_ROUTELEAKING))
            return Spines(
                spineNodeSelector=_spineNodeSelector,
                systemPoolIPV4=_systemPoolIPV4,
                systemPoolIPV6=_systemPoolIPV6,
                asnPool=_asnPool,
                routeLeaking=_routeLeaking,
            )
        return None  # pragma: no cover


class SuperSpines:
    def __init__(
        self,
        superSpineNodeSelector: list[str] | None = None,
        systemPoolIPV4: str | None = None,
        systemPoolIPV6: str | None = None,
        asnPool: str | None = None,
        routeLeaking: RouteLeaking | None = None,
    ):
        self.superSpineNodeSelector = superSpineNodeSelector
        self.systemPoolIPV4 = systemPoolIPV4
        self.systemPoolIPV6 = systemPoolIPV6
        self.asnPool = asnPool
        self.routeLeaking = routeLeaking

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.superSpineNodeSelector is not None:
            _rval[Y_SUPERSPINENODESELECTOR] = self.superSpineNodeSelector
        if self.systemPoolIPV4 is not None:
            _rval[Y_SYSTEMPOOLIPV4] = self.systemPoolIPV4
        if self.systemPoolIPV6 is not None:
            _rval[Y_SYSTEMPOOLIPV6] = self.systemPoolIPV6
        if self.asnPool is not None:
            _rval[Y_ASNPOOL] = self.asnPool
        if self.routeLeaking is not None:
            _rval[Y_ROUTELEAKING] = self.routeLeaking.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> "SuperSpines | None":
        if obj:
            _superSpineNodeSelector = obj.get(Y_SUPERSPINENODESELECTOR)
            _systemPoolIPV4 = obj.get(Y_SYSTEMPOOLIPV4)
            _systemPoolIPV6 = obj.get(Y_SYSTEMPOOLIPV6)
            _asnPool = obj.get(Y_ASNPOOL)
            _routeLeaking = RouteLeaking.from_input(obj.get(Y_ROUTELEAKING))
            return SuperSpines(
                superSpineNodeSelector=_superSpineNodeSelector,
                systemPoolIPV4=_systemPoolIPV4,
                systemPoolIPV6=_systemPoolIPV6,
                asnPool=_asnPool,
                routeLeaking=_routeLeaking,
            )
        return None  # pragma: no cover


class UnderlayBGP:
    def __init__(
        self,
        exportPolicy: list[str] | None = None,
        importPolicy: list[str] | None = None,
        asnPool: str | None = None,
        timers: Timers | None = None,
        keychain: str | None = None,
    ):
        self.exportPolicy = exportPolicy
        self.importPolicy = importPolicy
        self.asnPool = asnPool
        self.timers = timers
        self.keychain = keychain

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.exportPolicy is not None:
            _rval[Y_EXPORTPOLICY] = self.exportPolicy
        if self.importPolicy is not None:
            _rval[Y_IMPORTPOLICY] = self.importPolicy
        if self.asnPool is not None:
            _rval[Y_ASNPOOL] = self.asnPool
        if self.timers is not None:
            _rval[Y_TIMERS] = self.timers.to_input()
        if self.keychain is not None:
            _rval[Y_KEYCHAIN] = self.keychain
        return _rval

    @staticmethod
    def from_input(obj) -> "UnderlayBGP | None":
        if obj:
            _exportPolicy = obj.get(Y_EXPORTPOLICY)
            _importPolicy = obj.get(Y_IMPORTPOLICY)
            _asnPool = obj.get(Y_ASNPOOL)
            _timers = Timers.from_input(obj.get(Y_TIMERS))
            _keychain = obj.get(Y_KEYCHAIN)
            return UnderlayBGP(
                exportPolicy=_exportPolicy,
                importPolicy=_importPolicy,
                asnPool=_asnPool,
                timers=_timers,
                keychain=_keychain,
            )
        return None  # pragma: no cover


class UnderlayOSPF:
    def __init__(
        self,
        addressFamily: list[str],
    ):
        self.addressFamily = addressFamily

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.addressFamily is not None:
            _rval[Y_ADDRESSFAMILY] = self.addressFamily
        return _rval

    @staticmethod
    def from_input(obj) -> "UnderlayOSPF | None":
        if obj:
            _addressFamily = obj.get(Y_ADDRESSFAMILY)
            return UnderlayOSPF(
                addressFamily=_addressFamily,
            )
        return None  # pragma: no cover


class UnderlayProtocol:
    def __init__(
        self,
        protocol: list[str],
        bfd: BFD | None = None,
        bgp: UnderlayBGP | None = None,
        ospf: UnderlayOSPF | None = None,
    ):
        self.protocol = protocol
        self.bfd = bfd
        self.bgp = bgp
        self.ospf = ospf

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.protocol is not None:
            _rval[Y_PROTOCOL] = self.protocol
        if self.bfd is not None:
            _rval[Y_BFD] = self.bfd.to_input()
        if self.bgp is not None:
            _rval[Y_BGP] = self.bgp.to_input()
        if self.ospf is not None:
            _rval[Y_OSPF] = self.ospf.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> "UnderlayProtocol | None":
        if obj:
            _protocol = obj.get(Y_PROTOCOL)
            _bfd = BFD.from_input(obj.get(Y_BFD))
            _bgp = UnderlayBGP.from_input(obj.get(Y_BGP))
            _ospf = UnderlayOSPF.from_input(obj.get(Y_OSPF))
            return UnderlayProtocol(
                protocol=_protocol,
                bfd=_bfd,
                bgp=_bgp,
                ospf=_ospf,
            )
        return None  # pragma: no cover


class FabricSpec:
    def __init__(
        self,
        systemPoolIPV4: str | None = None,
        systemPoolIPV6: str | None = None,
        leafs: Leafs | None = None,
        spines: Spines | None = None,
        superSpines: SuperSpines | None = None,
        borderLeafs: BorderLeafs | None = None,
        interSwitchLinks: InterSwitchLinks | None = None,
        underlayProtocol: UnderlayProtocol | None = None,
        overlayProtocol: OverlayProtocol | None = None,
        fabricSelector: list[str] | None = None,
        routeLeaking: RouteLeaking | None = None,
    ):
        self.systemPoolIPV4 = systemPoolIPV4
        self.systemPoolIPV6 = systemPoolIPV6
        self.leafs = leafs
        self.spines = spines
        self.superSpines = superSpines
        self.borderLeafs = borderLeafs
        self.interSwitchLinks = interSwitchLinks
        self.underlayProtocol = underlayProtocol
        self.overlayProtocol = overlayProtocol
        self.fabricSelector = fabricSelector
        self.routeLeaking = routeLeaking

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.systemPoolIPV4 is not None:
            _rval[Y_SYSTEMPOOLIPV4] = self.systemPoolIPV4
        if self.systemPoolIPV6 is not None:
            _rval[Y_SYSTEMPOOLIPV6] = self.systemPoolIPV6
        if self.leafs is not None:
            _rval[Y_LEAFS] = self.leafs.to_input()
        if self.spines is not None:
            _rval[Y_SPINES] = self.spines.to_input()
        if self.superSpines is not None:
            _rval[Y_SUPERSPINES] = self.superSpines.to_input()
        if self.borderLeafs is not None:
            _rval[Y_BORDERLEAFS] = self.borderLeafs.to_input()
        if self.interSwitchLinks is not None:
            _rval[Y_INTERSWITCHLINKS] = self.interSwitchLinks.to_input()
        if self.underlayProtocol is not None:
            _rval[Y_UNDERLAYPROTOCOL] = self.underlayProtocol.to_input()
        if self.overlayProtocol is not None:
            _rval[Y_OVERLAYPROTOCOL] = self.overlayProtocol.to_input()
        if self.fabricSelector is not None:
            _rval[Y_FABRICSELECTOR] = self.fabricSelector
        if self.routeLeaking is not None:
            _rval[Y_ROUTELEAKING] = self.routeLeaking.to_input()
        return _rval

    @staticmethod
    def from_input(obj) -> "FabricSpec | None":
        if obj:
            _systemPoolIPV4 = obj.get(Y_SYSTEMPOOLIPV4)
            _systemPoolIPV6 = obj.get(Y_SYSTEMPOOLIPV6)
            _leafs = Leafs.from_input(obj.get(Y_LEAFS))
            _spines = Spines.from_input(obj.get(Y_SPINES))
            _superSpines = SuperSpines.from_input(obj.get(Y_SUPERSPINES))
            _borderLeafs = BorderLeafs.from_input(obj.get(Y_BORDERLEAFS))
            _interSwitchLinks = InterSwitchLinks.from_input(obj.get(Y_INTERSWITCHLINKS))
            _underlayProtocol = UnderlayProtocol.from_input(obj.get(Y_UNDERLAYPROTOCOL))
            _overlayProtocol = OverlayProtocol.from_input(obj.get(Y_OVERLAYPROTOCOL))
            _fabricSelector = obj.get(Y_FABRICSELECTOR)
            _routeLeaking = RouteLeaking.from_input(obj.get(Y_ROUTELEAKING))
            return FabricSpec(
                systemPoolIPV4=_systemPoolIPV4,
                systemPoolIPV6=_systemPoolIPV6,
                leafs=_leafs,
                spines=_spines,
                superSpines=_superSpines,
                borderLeafs=_borderLeafs,
                interSwitchLinks=_interSwitchLinks,
                underlayProtocol=_underlayProtocol,
                overlayProtocol=_overlayProtocol,
                fabricSelector=_fabricSelector,
                routeLeaking=_routeLeaking,
            )
        return None  # pragma: no cover


class Node:
    def __init__(
        self,
        node: str | None = None,
        operatingSystem: str | None = None,
        operatingSystemVersion: str | None = None,
        underlayAutonomousSystem: int | None = None,
    ):
        self.node = node
        self.operatingSystem = operatingSystem
        self.operatingSystemVersion = operatingSystemVersion
        self.underlayAutonomousSystem = underlayAutonomousSystem

    def to_input(self):  # pragma: no cover
        _rval = {}
        if self.node is not None:
            _rval[Y_NODE] = self.node
        if self.operatingSystem is not None:
            _rval[Y_OPERATINGSYSTEM] = self.operatingSystem
        if self.operatingSystemVersion is not None:
            _rval[Y_OPERATINGSYSTEMVERSION] = self.operatingSystemVersion
        if self.underlayAutonomousSystem is not None:
            _rval[Y_UNDERLAYAUTONOMOUSSYSTEM] = self.underlayAutonomousSystem
        return _rval

    @staticmethod
    def from_input(obj) -> "Node | None":
        if obj:
            _node = obj.get(Y_NODE)
            _operatingSystem = obj.get(Y_OPERATINGSYSTEM)
            _operatingSystemVersion = obj.get(Y_OPERATINGSYSTEMVERSION)
            _underlayAutonomousSystem = obj.get(Y_UNDERLAYAUTONOMOUSSYSTEM)
            return Node(
                node=_node,
                operatingSystem=_operatingSystem,
                operatingSystemVersion=_operatingSystemVersion,
                underlayAutonomousSystem=_underlayAutonomousSystem,
            )
        return None  # pragma: no cover


class FabricStatus:
    def __init__(
        self,
        health: int | None = None,
        healthScoreReason: str | None = None,
        operationalState: str | None = None,
        lastChange: str | None = None,
        leafNodes: list[Node] | None = None,
        borderLeafNodes: list[Node] | None = None,
        spineNodes: list[Node] | None = None,
        superSpineNodes: list[Node] | None = None,
    ):
        self.health = health
        self.healthScoreReason = healthScoreReason
        self.operationalState = operationalState
        self.lastChange = lastChange
        self.leafNodes = leafNodes
        self.borderLeafNodes = borderLeafNodes
        self.spineNodes = spineNodes
        self.superSpineNodes = superSpineNodes

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
        if self.leafNodes is not None:
            _rval[Y_LEAFNODES] = [x.to_input() for x in self.leafNodes]
        if self.borderLeafNodes is not None:
            _rval[Y_BORDERLEAFNODES] = [x.to_input() for x in self.borderLeafNodes]
        if self.spineNodes is not None:
            _rval[Y_SPINENODES] = [x.to_input() for x in self.spineNodes]
        if self.superSpineNodes is not None:
            _rval[Y_SUPERSPINENODES] = [x.to_input() for x in self.superSpineNodes]
        return _rval

    @staticmethod
    def from_input(obj) -> "FabricStatus | None":
        if obj:
            _health = obj.get(Y_HEALTH)
            _healthScoreReason = obj.get(Y_HEALTHSCOREREASON)
            _operationalState = obj.get(Y_OPERATIONALSTATE)
            _lastChange = obj.get(Y_LASTCHANGE)
            _leafNodes = []
            if obj.get(Y_LEAFNODES) is not None:
                for x in obj.get(Y_LEAFNODES):
                    _leafNodes.append(Node.from_input(x))
            _borderLeafNodes = []
            if obj.get(Y_BORDERLEAFNODES) is not None:
                for x in obj.get(Y_BORDERLEAFNODES):
                    _borderLeafNodes.append(Node.from_input(x))
            _spineNodes = []
            if obj.get(Y_SPINENODES) is not None:
                for x in obj.get(Y_SPINENODES):
                    _spineNodes.append(Node.from_input(x))
            _superSpineNodes = []
            if obj.get(Y_SUPERSPINENODES) is not None:
                for x in obj.get(Y_SUPERSPINENODES):
                    _superSpineNodes.append(Node.from_input(x))
            return FabricStatus(
                health=_health,
                healthScoreReason=_healthScoreReason,
                operationalState=_operationalState,
                lastChange=_lastChange,
                leafNodes=_leafNodes,
                borderLeafNodes=_borderLeafNodes,
                spineNodes=_spineNodes,
                superSpineNodes=_superSpineNodes,
            )
        return None  # pragma: no cover


class Fabric:
    def __init__(
        self, metadata: Metadata | None = None, spec: FabricSpec | None = None, status: FabricStatus | None = None
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
    def from_input(obj) -> "Fabric | None":
        if obj:
            _metadata = (
                Metadata.from_input(obj.get(Y_METADATA))
                if obj.get(Y_METADATA, None)
                else Metadata.from_name(obj.get(Y_NAME))
            )
            _spec = FabricSpec.from_input(obj.get(Y_SPEC, None))
            _status = FabricStatus.from_input(obj.get(Y_STATUS))
            return Fabric(
                metadata=_metadata,
                spec=_spec,
                status=_status,
            )
        return None  # pragma: no cover


class FabricList:
    def __init__(self, items: list[Fabric], listMeta: object | None = None):
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
    def from_input(obj) -> "FabricList | None":
        if obj:
            _items = obj.get(Y_ITEMS, [])
            _listMeta = obj.get(Y_METADATA, None)
            return FabricList(
                items=_items,
                listMeta=_listMeta,
            )
        return None  # pragma: no cover
