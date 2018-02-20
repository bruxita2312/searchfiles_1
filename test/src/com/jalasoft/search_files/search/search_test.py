"""""
This module contain the unit tests for the search module
"""""
import pytest

from definition import CONFIG_PATH
from src.com.jalasoft.search_files.search.search import Search, size_converter_to_bytes
from src.com.jalasoft.search_files.utils.search_logging import logger


@pytest.mark.search
def test_a_Search_is_created():
    """
    testing that utils object is being created
    """
    logger.info(">>> Unit Test: Search  object is created .... starting")
    search_test = Search()
    assert isinstance(search_test, Search)
    logger.info(">>> test_a_Search_is_created: PASSED")


@pytest.mark.search
def test_set_options():
    """
    testing that utils object is being created
    """
    logger.info(">>> Unit Test: Search  object is created .... starting")
    search_test = Search()
    expected1 = {"search_path": "/Users/dxnis/Documents/pruebamenu", "search_on": "file",
                 "search_size": size_converter_to_bytes(14.0066, "mb"), "search_size_options": "Equal"}
    expected2 = {"search_path": "/Users/dxnis/Documents/pruebamenu", "search_on": "file",
                 "search_size": size_converter_to_bytes(950, "mb"), "search_size_options": "Greater"}
    expected3 = {"search_path": "/Users/dxnis/Documents/pruebamenu", "search_on": "file",
                 "search_size": size_converter_to_bytes(35, "mb"), "search_size_options": "Smaller"}

    search_criteria_using_set = search_test.set_options(expected1)
    assert (search_criteria_using_set, expected1)
    search_criteria_using_set = search_test.set_options(expected2)
    assert (search_criteria_using_set, expected2)
    search_criteria_using_set = search_test.set_options(expected3)
    assert (search_criteria_using_set, expected3)
    logger.error(">>> test Window height size, is valid: PASSED")


@pytest.mark.search
def test_set_options():
    """
    testing that utils object is being created
    """
    logger.info(">>> Unit Test: Search  object is created .... starting")
    search_test = Search()

    criteria1 = {"search_path": "/Users/dxnis/Documents/pruebamenu", "search_on": "file",
                 "search_size": size_converter_to_bytes(14.0066, "mb"), "search_size_options": "Equal"}
    criteria2 = {"search_path": "/Users/dxnis/Documents/pruebamenu", "search_on": "file",
                 "search_size": size_converter_to_bytes(950, "mb"), "search_size_options": "Greater"}
    criteria3 = {"search_path": "/Users/dxnis/Documents/pruebamenu", "search_on": "file",
                 "search_size": size_converter_to_bytes(35, "mb"), "search_size_options": "Smaller"}

    assert (search_test.get_options() != None)
    assert not (search_test.get_options() == criteria1)
    assert not (search_test.get_options() == None)
    assert not (search_test.get_options() == "asdf")
    assert not (search_test.get_options() == 1111)


@pytest.mark.search
def testasdf():
    path = CONFIG_PATH + "r.txt"
    path1 = CONFIG_PATH + "r.1t"

    logger.info(">>> Unit Test: search_by_extension  is validated .... starting")
    search_test = Search()
    assert search_test.search_by_extension(path)
    assert search_test.search_by_extension(path1)
    logger.info(">>> Verifying that it is file: PASSED")


@pytest.mark.search
def testasdf():
    path = "asdfasdfasdfasdf"
    path1 = 1236
    path2 = None
    path10 = 12.36
    path5 = CONFIG_PATH

    logger.info(">>> Unit Test: search_by_extension is validated to values.... starting")
    search_test = Search()

    assert (search_test.search_by_extension(path), False)
    assert (search_test.search_by_extension(path10), False)
    assert (search_test.search_by_extension(path1), False)
    assert (search_test.search_by_extension(path2), False)
    assert (search_test.search_by_extension(path5), False)

    logger.info(">>> Verifying that it is not file: PASSED")
