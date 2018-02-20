"""""
This module contain the unit tests for the search_result module
"""""
import pytest

#from src.com.jalasoft.search_files.utils.search_util import import SearchUtilUtil
from src.com.jalasoft.search_files.utils.logging import logger


@pytest.mark.search_result
def test_a_SearchUtil():
    """
    testing that utils object is being created
    """
    logger.info(">>> test_a_SearchUtil_is_created: PASSED")
