#!/usr/bin/env python3
from common import constants

from .eda import EDAConfigHandler

_config_handlers = {constants.PLATFORM_EDA: EDAConfigHandler()}


def get_config_handler(platform_key):
    return _config_handlers[platform_key]
