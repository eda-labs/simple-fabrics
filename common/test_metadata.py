#!/usr/bin/env python3
"""Unit tests for EDA Metadata module"""

from common import metadata

INPUT_METADATA_NAME = "test-metadata"
INPUT_METADATA_DICT = {
    'name': INPUT_METADATA_NAME
}


def test_metadata_sanity():
    """Sanity test for class Metadata"""
    metadata_metadata = metadata.Metadata(INPUT_METADATA_NAME)
    assert metadata_metadata.name == INPUT_METADATA_NAME
    assert metadata_metadata.to_input() is None
    metadata_fromyaml = metadata.Metadata.from_yaml(INPUT_METADATA_DICT)
    assert isinstance(metadata_fromyaml, metadata.Metadata)
    assert metadata_fromyaml.name == metadata_metadata.name
    assert metadata.Metadata.from_yaml(None) is None
    assert metadata.Metadata.from_input(None) is None


if __name__ == "__main__":
    test_metadata_sanity()
