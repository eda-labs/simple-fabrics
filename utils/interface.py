#!/usr/bin/env python3
import utils.exceptions as e
from common.constants import PLATFORM_SRL, PLATFORM_SROS, PLATFORM_IOSXR, TAG_OS, PLATFORM_NXOS, PLATFORM_EOS

# Given a long subinterface name, return a interface name and subinterface index
# Ex:
#   input => "ethernet-1/1.0", output => "ethernet-1/1", "0"


# SR Linux speeds:
#   1G, 10G, 25G, 40G, 50G, 100G, 200G, 400G
#
# SROS speeds:
#   1000, 10000, 25000, 40000, 50000, 100000, 200000, 400000
# EOS speeds
# SPEED_10MB, SPEED_1GB, SPEED_2500MB
def get_normalized_speed(speed: str, os: str) -> int:
    if os == PLATFORM_SRL or os == PLATFORM_NXOS:
        if 'G' in speed:
            return int(speed.replace('G', '000000000'))
        else:
            return int(speed)
    elif os == PLATFORM_EOS:
        parts = speed.split('_')
        if len(parts) >= 2 and parts[0] == "SPEED":
            value_str = parts[1][:-2]
            unit = parts[1][-2:].upper()
            value = float(value_str)
            if unit == "KB":
                return int(value * 1000)
            elif unit == "MB":
                return int(value * 1000000)
            else:
                return int(value * 1000000000)
        else:
            return 0
    elif os == PLATFORM_SROS:
        return int(speed) * 1000000
        # if isinstance(speed, (int, float)):
        #     speed_str = str(speed) + '000000'
        #     return int(speed_str)
        # else:
        #     return speed


def get_human_readable_speed(normalized_speed: int) -> str:
    if normalized_speed == 0:
        return 'N/A'
    if normalized_speed >= 1000000000:
        return f'{normalized_speed//1000000000}G'
    elif normalized_speed >= 1000000:
        return f'{normalized_speed//1000000}M'
    elif normalized_speed >= 1000:
        return f'{normalized_speed//1000}K'
    else:
        return f'{normalized_speed}'


def get_interface_and_subinterface_index(subif_name):
    interface_parts = subif_name.split('.')
    if len(interface_parts) == 2:
        return interface_parts[0], interface_parts[1]
    else:
        return interface_parts[0], None

# Given a long name, return the short name
# Ex:
#   input => "ethernet-1/1", output => e1-1


def get_short_name(ifname):
    short_name = ifname.replace('ethernet-', 'e')
    short_name = short_name.replace('/', '-')
    return short_name

# parse interface name
# Ex:
#   input => "dut1-ethernet-1-1", output => False, True, "ethernet-1/1", dut1
#   input => "lag-lagexample", output => True, False, "lagexample", None


def get_interface_info(ifname):
    isLag = False
    isInterface = False

    if ifname.startswith('lag-'):
        isLag = True
        parts = ifname.split('-', 1)
        return isLag, isInterface, parts[1], None
    elif '-ethernet-' in ifname:
        isInterface = True
        parts = ifname.split('-ethernet-')
        if len(parts) == 2:
            return isLag, isInterface, f"ethernet-{parts[1].replace('-','/')}", parts[0]
        else:
            raise e.InvalidInput(f"Invalid interface name:{ifname}")  # pragma: no cover
    else:
        raise e.InvalidInput(f"Invalid interface name:{ifname}")  # pragma: no cover


def get_lag_name(lagid, node_os):
    if node_os == PLATFORM_SROS:
        return f'lag-{lagid}'
    return f'lag{lagid}'


def get_node_interface_info(norm_intf_name, node_cr, isLoopback=False):
    node_os = node_cr['spec'].get(TAG_OS)
    if node_os == PLATFORM_SROS:
        return to_sros_interface(norm_intf_name, node_cr, isLoopback=isLoopback)
    elif node_os == PLATFORM_IOSXR:
        return to_iosxr_interface(norm_intf_name, node_cr, isLoopback=isLoopback)
    elif node_os == PLATFORM_NXOS:
        return to_nxos_interface(norm_intf_name, node_cr, isLoopback=isLoopback)
    elif node_os == PLATFORM_EOS:
        return to_eos_interface(norm_intf_name, node_cr, isLoopback=isLoopback)
    return to_srl_interface(norm_intf_name, node_cr, isLoopback=isLoopback)


# Normalized interface name to SRL interface names:
# ethernet-1-1 => ethernet-1/1 for single mda and ethernet-1/a/1 for multi mda (future)
# ethernet-2-1 => ethernet-2/1 for single mda ethernet-2/a/1 for multi mda (future)
# ethernet-2-b-1 =>  ethernet-2/b/1 for multi mda (future)
# ethernet-1-1-1 (breakout) => ethernet-1/1/1 for single mda, ethernet-1/a/1/1 for multi mda (future)
# ethernet-2-b-1-1 (breakout) = > ethernet-2/b/1/1 for multi mda (future)
def to_srl_interface(norm_intf_name: str, node_cr, isLoopback=False):
    parts = norm_intf_name.split('-', 1)
    srl_name = parts[0]
    if len(parts) > 1:
        if 'lag' in norm_intf_name:
            srl_name = f'lag{parts[1]}'
        else:
            # current SRL linecards does not support multiple MDAs,
            srl_name = f"{parts[0]}-{parts[1].replace('-', '/')}"
        # add logic based on SRL platform when linecard will support multiple MDAs(future)
    if isLoopback is True:
        if parts[0] == 'loopback' and parts[1].isdigit():
            srl_name = f'lo{parts[1]}'

    return srl_name, f'.interface{{.name=="{srl_name}"}}', f'.interface{{.name=="{srl_name}"}}'


def to_eos_interface(norm_intf_name: str, node_cr, isLoopback=False):
    parts = norm_intf_name.split('-')
    eos_name = parts[0]
    if len(parts) == 3:
        eos_name = f"Ethernet{parts[1]}/{parts[2]}"
    if isLoopback is True:
        if parts[0] == 'loopback' and parts[1].isdigit():
            eos_name = f'Loopback{parts[1]}'

    return eos_name, f'.interfaces.interface{{.name=="{eos_name}"}}', f'.interfaces.interface{{.name=="{eos_name}"}}'


# Normalized interface name to SROS interface names:
# ethernet-1-1 => 1/1/1
# ethernet-2-1 => 2/1/1
# ethernet-2-b-1 => 2/2/1
# ethernet-1-1-1 (breakout) => 1/1/c2/1 based on platform or card type
# ethernet-2-b-1-1 (breakout) = > 2/2/c2/1 based on platform or card type
# ethernet-1-1-a-1 => 1/x1/1/1
# ethernet-1-1-b-1-1 => 1/x1/2/c1/1 breakout
def to_sros_interface(norm_intf_name: str, node_cr, isLoopback=False):
    parts = norm_intf_name.split('-')
    sros_name = norm_intf_name
    config_path = ''
    state_path = ''
    is_xiom_mda = False
    mda_id = '1'
    linecard_id = '1'
    xiom_id = None
    port_id = ''

    if 'lag' in norm_intf_name:
        config_path = f'.configure.lag{{.lag-name=="{sros_name}"}}'
        state_path = f'.state.lag{{.lag-name=="{sros_name}"}}'
    elif parts[0] == 'system0':
        sros_name = 'system'
        config_path = f'.configure.router{{.router-name=="Base"}}.interface{{.interface-name=="{sros_name}"}}'
        state_path = f'.state.router{{.router-name=="Base"}}.interface{{.interface-name=="{sros_name}"}}'
    elif isLoopback is True:
        if parts[0] == 'loopback' and parts[1].isdigit():
            sros_name = f'lo{parts[1]}'
    else:
        if len(parts) > 4 and parts[3].isalpha():
            # ethernet-1-1-a-1 => 1/x1/1/1
            # ethernet-1-1-b-1-1 => 1/x1/2/c1/1 breakout
            is_xiom_mda = True
            mda_id = ord(parts[3].upper()) - 64
            linecard_id = parts[1]
            xiom_id = f'x{parts[2]}'
            if len(parts) == 5:
                port_id = parts[4]
            else:
                port_id = f'c{parts[4]}/{parts[5]}'
        elif len(parts) > 2:
            linecard_id = parts[1]
            # ethernet-2-b-1 => 2/2/1
            # ethernet-2-b-1-1 => 2/2/c1/1 breakout
            if parts[2].isalpha():
                mda_id = ord(parts[2].upper()) - 64
                if len(parts) == 4:
                    port_id = parts[3]
                elif len(parts) == 5:
                    port_id = f'c{parts[3]}/{parts[4]}'
            else:
                # ethernet-1-1-1  => 1/1/c1/1 breakout
                # ethernet-1-1 => 1/1/1
                # mda_id = 1 # already initialised.
                if len(parts) == 3:
                    port_id = parts[2]
                elif len(parts) == 4:
                    port_id = f'c{parts[2]}/{parts[3]}'
        # construct sros name.
        if len(port_id) != 0:
            if is_xiom_mda is True:
                sros_name = f'{linecard_id}/{xiom_id}/{mda_id}/{port_id}'
            else:
                sros_name = f'{linecard_id}/{mda_id}/{port_id}'

        config_path = f'.configure.port{{.port-id=="{sros_name}"}}'
        state_path = f'.state.port{{.port-id=="{sros_name}"}}'

    return sros_name, config_path, state_path

# Note: Cisco IOS-XR is 0 based
# Note: Need to add function to look at port speed to determine name correctly
# Normalized interface name to IOS-XR interface names:
# ethernet-1-1 => GigabitEthernet0/0/0/0
# ethernet-1-2 => GigabitEthernet0/0/0/1
# ethernet-2-1 => GigabitEthernet0/1/0/0
# ethernet-2-b-1 =>  GigabitEthernet0/1/1/0 for multi mda


def to_iosxr_interface(norm_intf_name: str, node_cr, isLoopback=False):  # pragma: no cover
    parts = norm_intf_name.split('-')
    if parts[0] != 'system0':
        # Subtract 1 from the slot and port number as IOS-XR is 0-based
        slot = int(parts[1]) - 1
        port = int(parts[2]) - 1 if len(parts) > 2 else 0
    iosxr_name = None
    if len(parts) == 3:
        # Format: ethernet-X-Y
        # Maps to: GigabitEthernet0/X/0/Y
        iosxr_name = f"GigabitEthernet0/{slot}/0/{port}"
    elif len(parts) == 4 and parts[2].isalpha():
        # Format: ethernet-X-b-Y (multi MDA)
        # Maps to: GigabitEthernet0/X/1/Y
        iosxr_name = f"GigabitEthernet0/{slot}/1/{port}"
    elif parts[0] == 'system0':
        iosxr_name = 'Loopback0'
    if iosxr_name:
        config_path = f'.interfaces.interface{{.name=="{iosxr_name}"}}'
        return iosxr_name, config_path, config_path
    return None, None, None


def to_nxos_interface(norm_intf_name: str, node_cr, isLoopback=False):  # pragma: no cover
    parts = norm_intf_name.split('-')
    nxos_name = parts[0]
    if len(parts) == 3:
        # Format: ethernet-X-Y
        # Maps to: EthernetX/Y
        nxos_name = f"eth{parts[1]}/{parts[2]}"
    elif parts[0] == 'system0':
        nxos_name = 'Loopback0'
    if nxos_name:
        config_path = f'.System.intf-items.phys-items.PhysIf-list{{.id=="{nxos_name}"}}'
        return nxos_name, config_path, config_path
    return None, None, None
