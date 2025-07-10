#!/usr/bin/env python3
import eda_common as eda

import simple_fabrics.api.v1alpha1.pysrc.constants as c
import utils.exceptions as e
import utils.node_utils as nutils
from common.constants import PLATFORM_EDA
from simple_fabrics.api.v1alpha1.pysrc.simplefabric import SimpleFabric
from simple_fabrics.intents.simplefabric.handlers import get_config_handler
from simple_fabrics.intents.simplefabric.init import init_globals_defaults, validate
from utils.log import log_msg


def process_cr(cr):
    """Process SimpleFabric CR."""
    sf = SimpleFabric.from_input(cr)
    if sf is None:
        return

    validate(sf)
    init_globals_defaults(sf)

    eda_handler = get_config_handler(PLATFORM_EDA)
    eda_handler.handle_cr(sf)
