"""""
This module contain the unit tests for the search module
"""""
import pytest

from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.utils.logging import logger


@pytest.mark.search
def test_a_Search_is_created():
    """
    testing that utils object is being created
    """
    search_test = Search()
    assert isinstance(search_test, Search)
    logger.info(">>> test_a_Search_is_created: PASSED")