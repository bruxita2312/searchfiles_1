"""""
This module contain the unit tests for the search_result module
"""""
import pytest

import src.com.jalasoft.search_files.utils.search_util as utils
from src.com.jalasoft.search_files.utils.search_logging import logger


@pytest.mark.search_util
def test_to_validate_type_file():
    """
    testing that the file type to convert, is valid
    """
    type_tb = "tb"
    type_gb = "gb"
    type_mb = "mb"
    type_kb = "kb"

    assert utils.size_converter_to_bytes(2, str(type_tb) == 2048)
    assert utils.size_converter_to_bytes(2, str(type_gb) == 2048)
    assert utils.size_converter_to_bytes(2, str(type_mb) == 2048)
    assert utils.size_converter_to_bytes(2, str(type_kb) == 2048)

    logger.info(">>> test that the file type to convert, is valid: PASSED")

@pytest.mark.search_util
def test_to_validate_type_file():
    """
    testing that the size to convert, is valid
    """
    type_tb = "tb"
    type_gb = "gb"
    type_mb = "mb"
    type_kb = "kb"

    assert utils.size_converter_to_bytes(2, str(type_tb) == 2048)
    assert utils.size_converter_to_bytes(2, str(type_gb) == 2048)
    assert utils.size_converter_to_bytes(2, str(type_mb) == 2048)
    assert utils.size_converter_to_bytes(2, str(type_kb) == 2048)
    assert utils.size_converter_to_bytes(20.456, str(type_tb) == 20946.944)
    assert utils.size_converter_to_bytes(20.456, str(type_gb) == 20946.944)
    assert utils.size_converter_to_bytes(20.456, str(type_mb) == 20946.944)
    assert utils.size_converter_to_bytes(20.456, str(type_kb) == 20946.944)
    assert not utils.size_converter_to_bytes(0, str(type_tb) == 0)
    assert not utils.size_converter_to_bytes(0, str(type_gb) == 0)
    assert not utils.size_converter_to_bytes(0, str(type_mb) == 0)
    assert not utils.size_converter_to_bytes(0, str(type_kb) == 0)
    logger.info(">>> test that the file type to convert, is valid: PASSED")
