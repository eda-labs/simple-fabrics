#!/usr/bin/env python3
"""Unit tests for EDA interfaces"""

from utils import interface

INPUT_INTERFACE_NAME = "dut1-ethernet-1/1"
INPUT_SUBINTERFACE_NAME = "subif0"
INPUT_LAG_NAME = "lag-lagexample"


def test_get_human_readable_speed():
    """Sanity test for function get_human_readable_speed"""
    assert interface.get_human_readable_speed(0) == "N/A"
    assert interface.get_human_readable_speed(100000000000) == "100G"
    assert interface.get_human_readable_speed(10000000000) == "10G"
    assert interface.get_human_readable_speed(1000000000) == "1G"
    assert interface.get_human_readable_speed(1000000) == "1M"
    assert interface.get_human_readable_speed(1000) == "1K"
    assert interface.get_human_readable_speed(100) == "100"


def test_get_normalized_speed():
    """Sanity test for function get_normalized_speed"""
    assert interface.get_normalized_speed("1G", "srl") == 1000000000
    assert interface.get_normalized_speed("10G", "srl") == 10000000000
    assert interface.get_normalized_speed("100G", "srl") == 100000000000
    assert interface.get_normalized_speed("1000", "sros") == 1000000000
    assert interface.get_normalized_speed("10000", "sros") == 10000000000
    assert interface.get_normalized_speed("100000", "sros") == 100000000000


def test_get_interface_and_subinterface_index_sanity():
    """Sanity test for function get_interface_and_subinterface_index"""
    interface_parts_1 = interface.get_interface_and_subinterface_index(INPUT_INTERFACE_NAME)
    assert interface_parts_1 == (INPUT_INTERFACE_NAME, None)
    interface_parts_2 = interface.get_interface_and_subinterface_index(f'{INPUT_INTERFACE_NAME}.{INPUT_SUBINTERFACE_NAME}')
    assert interface_parts_2 == (INPUT_INTERFACE_NAME, INPUT_SUBINTERFACE_NAME)


def test_get_short_name():
    """Sanity test for function get_short_name"""
    assert interface.get_short_name(INPUT_INTERFACE_NAME) == "dut1-e1-1"


def test_get_interface_info_interface_sanity():
    """Sanity test for function get_interface_info with interface input"""
    get_interface_info_tuple = interface.get_interface_info(INPUT_INTERFACE_NAME)
    assert len(get_interface_info_tuple) == 4
    assert get_interface_info_tuple[0] is False
    assert get_interface_info_tuple[1] is True
    assert get_interface_info_tuple[2] == "ethernet-1/1"
    assert get_interface_info_tuple[3] == "dut1"


def test_get_interface_info_lag_sanity():
    """Sanity test for function get_interface_info with lag input"""
    get_interface_info_tuple = interface.get_interface_info(INPUT_LAG_NAME)
    assert len(get_interface_info_tuple) == 4
    assert get_interface_info_tuple[0] is True
    assert get_interface_info_tuple[1] is False
    assert get_interface_info_tuple[2] == "lagexample"
    assert get_interface_info_tuple[3] is None


def test_to_srl_interface():
    """Sanity test for function to_srl_interface """
    itf_tuple = interface.to_srl_interface('ethernet-1-1', None)
    assert itf_tuple[0] == 'ethernet-1/1'
    assert itf_tuple[1] == '.interface{.name=="ethernet-1/1"}'
    itf_tuple = interface.to_srl_interface('ethernet-2-10', None)
    assert itf_tuple[0] == 'ethernet-2/10'
    assert itf_tuple[1] == '.interface{.name=="ethernet-2/10"}'
    itf_tuple = interface.to_srl_interface('ethernet-1-1-1', None)
    assert itf_tuple[0] == 'ethernet-1/1/1'
    assert itf_tuple[1] == '.interface{.name=="ethernet-1/1/1"}'
    itf_tuple = interface.to_srl_interface('ethernet-2-2-1', None)
    assert itf_tuple[0] == 'ethernet-2/2/1'
    assert itf_tuple[1] == '.interface{.name=="ethernet-2/2/1"}'
    itf_tuple = interface.to_srl_interface('system0', None)
    assert itf_tuple[0] == 'system0'
    assert itf_tuple[1] == '.interface{.name=="system0"}'
    itf_tuple = interface.to_srl_interface('lag10', None)
    assert itf_tuple[0] == 'lag10'
    assert itf_tuple[1] == '.interface{.name=="lag10"}'


def test_to_iosxr_interface():
    """Sanity test for function to_iosxr_interface """
    itf_tuple = interface.to_iosxr_interface('ethernet-1-1', None)
    assert itf_tuple[0] == 'GigabitEthernet0/0/0/0'
    assert itf_tuple[1] == '.interfaces.interface{.name=="GigabitEthernet0/0/0/0"}'
    itf_tuple = interface.to_iosxr_interface('ethernet-2-10', None)
    assert itf_tuple[0] == 'GigabitEthernet0/1/0/9'
    assert itf_tuple[1] == '.interfaces.interface{.name=="GigabitEthernet0/1/0/9"}'
    itf_tuple = interface.to_iosxr_interface('system0', None)
    assert itf_tuple[0] == 'Loopback0'
    assert itf_tuple[1] == '.interfaces.interface{.name=="Loopback0"}'


def test_to_sros_interface():
    """Sanity test for function to_sros_interface """
    itf_tuple = interface.to_sros_interface('ethernet-1-1', None)
    assert itf_tuple[0] == '1/1/1'
    assert itf_tuple[1] == '.configure.port{.port-id=="1/1/1"}'

    itf_tuple = interface.to_sros_interface('ethernet-2-10', None)
    assert itf_tuple[0] == '2/1/10'
    assert itf_tuple[1] == '.configure.port{.port-id=="2/1/10"}'

    itf_tuple = interface.to_sros_interface('ethernet-2-b-10', None)
    assert itf_tuple[0] == '2/2/10'
    assert itf_tuple[1] == '.configure.port{.port-id=="2/2/10"}'

    itf_tuple = interface.to_sros_interface('ethernet-1-1-1', None)
    assert itf_tuple[0] == '1/1/c1/1'
    assert itf_tuple[1] == '.configure.port{.port-id=="1/1/c1/1"}'

    itf_tuple = interface.to_sros_interface('ethernet-1-4-1', None)
    assert itf_tuple[0] == '1/1/c4/1'
    assert itf_tuple[1] == '.configure.port{.port-id=="1/1/c4/1"}'

    itf_tuple = interface.to_sros_interface('ethernet-2-2-1', None)
    assert itf_tuple[0] == '2/1/c2/1'
    assert itf_tuple[1] == '.configure.port{.port-id=="2/1/c2/1"}'

    itf_tuple = interface.to_sros_interface('ethernet-2-b-1-1', None)
    assert itf_tuple[0] == '2/2/c1/1'
    assert itf_tuple[1] == '.configure.port{.port-id=="2/2/c1/1"}'

    itf_tuple = interface.to_sros_interface('lag-10', None)
    assert itf_tuple[0] == 'lag-10'
    assert itf_tuple[1] == '.configure.lag{.lag-name=="lag-10"}'

    itf_tuple = interface.to_sros_interface('system0', None)
    assert itf_tuple[0] == 'system'
    assert itf_tuple[1] == '.configure.router{.router-name=="Base"}.interface{.interface-name=="system"}'

    itf_tuple = interface.to_sros_interface('ethernet-1-1-a-1', None)
    assert itf_tuple[0] == '1/x1/1/1'

    itf_tuple = interface.to_sros_interface('ethernet-2-2-b-10', None)
    assert itf_tuple[0] == '2/x2/2/10'

    itf_tuple = interface.to_sros_interface('ethernet-1-1-b-2-8', None)
    assert itf_tuple[0] == '1/x1/2/c2/8'

    itf_tuple = interface.to_sros_interface('ethernet-2-2-a-3-8', None)
    assert itf_tuple[0] == '2/x2/1/c3/8'


def test_get_lag_name():
    """Sanity test for function get_lag_name """
    assert interface.get_lag_name(20, 'srl') == "lag20"
    assert interface.get_lag_name(20, 'sros') == "lag-20"


if __name__ == "__main__":
    test_get_human_readable_speed()
    test_get_normalized_speed()
    test_get_interface_and_subinterface_index_sanity()
    test_get_short_name()
    test_get_interface_info_interface_sanity()
    test_get_interface_info_lag_sanity()
    test_to_srl_interface()
    # test_to_iosxr_interface()
    test_to_sros_interface()
    test_get_lag_name()
