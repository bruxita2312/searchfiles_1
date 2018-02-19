"""""
This module contain the unit tests for the validator module
"""""
import pytest

from src.com.jalasoft.search_files.utils.logging import logger
from src.com.jalasoft.search_files.validator.validator import Validator

@pytest.mark.validator
def test_a_validator_is_created():
    """
    verifying that validator object is created
    """
    validator_test = Validator()
    assert isinstance(validator_test, Validator)
    logger.info(">>> test_a_validator_is_created: PASSED")

#@pytest.mark.validator
#def test_is_a_valid_path():
    """
    Verifying that the path is correct
    """
#    logger.info(">>>>test_is_a_valid_path...... begin!")

#    path3 = 'C:\\Users'

#    assert Validator.is_path(path3, 4)
#    logger.info(">>> test_is_a_valid_path: PASSED")
