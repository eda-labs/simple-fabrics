#!/usr/bin/env python3

import eda_state as estate
from common.alarm_constants import SUBINTF_DOWN, BFD_SESSION_DOWN
from common.bfd import Peer

SESSION_UP = "UP"


class CrNameAndSchema:
    def __init__(
            self,
            cr_name: str,
            schema: any):
        self.cr_name = cr_name
        self.schema = schema


def raise_subinterfacedown_alarm(schema, resource_name: str, alarm_name: str, jspath: str, oper_down_reason: str):
    estate.update_alarm(
        name=alarm_name,
        alarm_type=SUBINTF_DOWN,
        severity='critical',
        resource=resource_name,
        kind=schema.kind,
        group=schema.group,
        description='This alarm is raised when the operational state of a subinterface is "down"',
        probable_cause=f'The subinterface is operationally down: {oper_down_reason}',
        remedial_action='Verify the operational state and health of the subinterface.',
        jspath=jspath
    )


def raise_bfd_session_down_alarm(schema, resource_name: str, local_address: str, session_state: str, jspath: str):
    alarm_name = f'{BFD_SESSION_DOWN}-{schema.kind}-{resource_name}-localaddr-{local_address}'
    estate.update_alarm(
        name=alarm_name,
        alarm_type=BFD_SESSION_DOWN,
        severity='critical',
        resource=resource_name,
        kind=schema.kind,
        group=schema.group,
        description='This alarm is raised when the BFD session associated with an interface is not "up"',
        probable_cause=f'BFD session is not up, session state: {session_state}',
        remedial_action='Verify the state of the BFD session.',
        jspath=jspath
    )


def process_bfd_session_states(node_name: str, bfd_session_states: list[Peer], intf_ips: dict[str], intf_names: dict[str]):
    for session in bfd_session_states:
        if session.is_session_up is not True:
            cr_name_schema = None
            # TODO (thadhani): Is there a better way to determine whether session is on link using unnumbered IPv6?
            # SROS has intf_name for both IPv4 and unnumbered IPv6 sessions, SRL has ipv6-link-local-interface only for unnumbered.
            # Should only look at the interface name for unnumbered IPv6? Or can we leave it like this?
            if session.intf_name is not None:
                node_link_local_intf = f'{node_name}:{session.intf_name}'
                cr_name_schema = intf_names.get(node_link_local_intf)
            else:
                cr_name_schema = intf_ips.get(session.local_address)
            if cr_name_schema is not None:
                raise_bfd_session_down_alarm(cr_name_schema.schema, cr_name_schema.cr_name, session.local_address, session.session_state, session.jspath)
