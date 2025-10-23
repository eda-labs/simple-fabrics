#!/usr/bin/env python3
import eda_common as eda

from common.constants import PLATFORM_EDA
from simple_fabrics.api.v1alpha1.pysrc.simplefabricstate import SimpleFabricState
from simple_fabrics.intents.simplefabricstate.init import init_globals_defaults, validate
from simple_fabrics.intents.simplefabricstate.state_handlers import get_state_handler
from utils.log import log_msg


def process_state_cr(cr):
    log_msg("SimpleFabricState CR:", dict=cr)
    cr_obj = SimpleFabricState.from_input(cr)
    if cr_obj is None:
        return
    validate(cr_obj)
    init_globals_defaults(cr_obj)
    handler = get_state_handler(PLATFORM_EDA)
    handler.handle_cr(cr_obj)
