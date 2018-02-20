"""""
This module contain the unit tests for the search_result module
"""""
import pytest

import src.com.jalasoft.search_files.utils.search_util as utils
from src.com.jalasoft.search_files.utils.logging import logger


@pytest.mark.search_util
def test_to_validate_type_file():
    """
    testing that the file type to convert, is valid
    """
    type_tb = "tb"
    type_gb = "gb"
    type_mb = "mb"
    wrong_type = 1555

    assert utils.size_converter_to_bytes(2, str(type_tb))
    assert utils.size_converter_to_bytes(2, str(type_gb))
    assert utils.size_converter_to_bytes(2, str(type_mb))

    logger.info(">>> test that the file type to convert, is valid: PASSED")
