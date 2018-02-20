"""""
This module contain the unit tests for the menu_main module
"""""
import pytest

from src.com.jalasoft.search_files.utils.logging import logger
from src.com.jalasoft.search_files.menu.menu_main import MenuMain


@pytest.mark.menu
def test_a_main_menu_is_created():
    """
    Verifying that  Menu Main object is created
    """
    logger.info(">>> Unit Test: Menu Main object is created .... starting")
    menu_main_test = MenuMain()
    assert isinstance(menu_main_test, MenuMain)
    logger.info(">>> Verifying that  Menu Main object is created: PASSED")
