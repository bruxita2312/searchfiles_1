"""""
This module contain the unit tests for the search_result module
"""""
import pytest

from src.com.jalasoft.search_files.utils.search_result import SearchResult
from src.com.jalasoft.search_files.utils.logging import logger


@pytest.mark.search_result
def test_a_SearchResult_is_created():
    """
    testing that utils object is being created
    """
    search_result_test = SearchResult()
    assert isinstance(search_result_test, SearchResult)
    logger.info(">>> test_a_SearchResult_is_created: PASSED")
