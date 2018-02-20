"""""
This module contain the unit tests for the search_result module
"""""
import pytest

from src.com.jalasoft.search_files.utils.search_result import SearchResult
from src.com.jalasoft.search_files.utils.search_logging import logger


@pytest.mark.search
def test_a_Search_is_created():
    """
    testing that utils object is being created
    """
    logger.info(">>> Unit Test: Search Result object is created .... starting")
    search_result_test = SearchResult()
    assert isinstance(search_result_test, SearchResult)
    logger.info(">>> test_a_Search_Result_is_created: PASSED")