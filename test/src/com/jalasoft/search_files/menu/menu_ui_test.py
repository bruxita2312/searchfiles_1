"""""
This module contain the unit tests for the menu_ui module
"""""
import pytest

from src.com.jalasoft.search_files.utils.logging import logger
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
