#!/usr/bin/env python3
import utils.exceptions as e
from simple_fabrics.api.v1alpha1.pysrc.simplefabric import SimpleFabric


def validate(cr: SimpleFabric):
    """Validate the given CR."""
    if cr.spec is None or cr.metadata is None:
        # handle error here or in the validate function
        raise e.InvalidInput("spec or metadata is not defined")


def init_globals_defaults(cr: SimpleFabric):
    """Initialize the global variables."""
    # implement this
    pass
