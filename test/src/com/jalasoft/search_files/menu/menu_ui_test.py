"""""
This module contain the unit tests for the menu_ui module
"""""
import pytest

from src.com.jalasoft.search_files.utils.search_logging import logger
from src.com.jalasoft.search_files.menu.menu_ui import Menu_UI


@pytest.mark.menu
def test_a_menu_ui_is_created():
    """
    Verifying that  Menu Main object is created
    """
    logger.info(">>> Unit Test: Menu UI object is created .... starting")
    menu_ui_test = Menu_UI()
    assert isinstance(menu_ui_test, Menu_UI)
    logger.info(">>> Verifying that  Menu UI object is created: PASSED")


@pytest.mark.menu
def test_window_with():
    """
    Verifying that
    """
    logger.info(">>> Unit Test: GetWindowWith.. .... starting")
    menu_ui_test = Menu_UI()
    assert (menu_ui_test.get_window_with() >= 300)
    assert (menu_ui_test.get_window_with() >= 1)
    assert (menu_ui_test.get_window_with() > 0)
    assert not (menu_ui_test.get_window_with() == 0)
    assert not (menu_ui_test.get_window_with() == None)
    assert not (menu_ui_test.get_window_with() == "asdf")
    logger.info(">>> test window with size, is valid: PASSED")


@pytest.mark.menu
def test_window_height():
    """
    Verifying that
    """
    logger.info(">>> Unit Test: GetWindow height.. .... starting")
    menu_ui_test = Menu_UI()
    assert (menu_ui_test.get_window_height() >= 100)
    assert not (menu_ui_test.get_window_height() >= 10000)
    assert (menu_ui_test.get_window_height() > 0)
    assert not (menu_ui_test.get_window_height() == 0)
    assert not (menu_ui_test.get_window_height() == "asdf")
    assert not (menu_ui_test.get_window_height() == None)
    logger.info(">>> test Window height size, is valid: PASSED")


@pytest.mark.menu
def test_format_title_frame():
    """
    Verifying that
    """
    logger.info(">>> Unit Test: format_title_frame .... starting")
    menu_ui_test = Menu_UI()
    assert (menu_ui_test.format_title_frame(), "sdf")
    assert (menu_ui_test.format_title_frame(), 132)
    logger.info(">>> test format_title_frame is valid: PASSED")


@pytest.mark.menu
def test_format_advance_frame():
    """
    Verifying that
    """
    logger.info(">>> Unit Test: format_advance_frame .... starting")
    menu_ui_test = Menu_UI()
    assert (menu_ui_test.format_advance_frame, "sdf")
    assert (menu_ui_test.format_advance_frame, 9999)
    logger.info(">>> test  format_advance_frame is valid: PASSED")


@pytest.mark.menu
def test_format_table_result():
    """
    Verifying that
    """
    logger.info(">>> Unit Test: format_advance_frame .... starting")
    menu_ui_test = Menu_UI()
    assert (menu_ui_test.format_table_result, None)

@pytest.mark.menu
def test_format_table_result():
    """
    Verifying that
    """
    logger.info(">>> Unit Test: format_advance_frame .... starting")
    menu_ui_test = Menu_UI()
    assert (menu_ui_test.format_table_result, None)