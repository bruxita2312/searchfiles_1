"""""
This module contain the unit tests for the validator module
"""""
import pytest
from definition import CONFIG_PATH
from src.com.jalasoft.search_files.utils.logging import logger
from src.com.jalasoft.search_files.validator.validator import Validator


@pytest.mark.validator
def test_a_validator_is_created():
    """
    Verifying that validator object is created
    """
    validator_test = Validator()
    assert isinstance(validator_test, Validator)
    logger.info(">>> Verifying that validator object is created: PASSED")


@pytest.mark.validator
def test_is_a_valid_path():
    """
    Verifying that the path is correct
    """
    validator_test = Validator()
    assert validator_test.is_path(CONFIG_PATH, 2)
    logger.info(">>> Verifying that the path is correct: PASSED")


@pytest.mark.validator
def test_is_a_invalid_path():
    """
    Verifying that the path is invalid
    """

    validator_test = Validator()

    invalid_path = CONFIG_PATH + '\\' + '@'

    assert not validator_test.is_path(invalid_path, 0)
    assert not validator_test.is_path(invalid_path, 1)
    assert not validator_test.is_path(invalid_path, 2)
    assert not validator_test.is_path(invalid_path, 3)
    assert not validator_test.is_path(invalid_path, 4)
    logger.info(">>> Verifying that the path is invalid: PASSED")


@pytest.mark.validator
def test_to_validate_try_counter():
    """
    Verifying that the try counter allows a maximum number of attempts.
    """

    validator_test = Validator()
    assert not validator_test.is_path(CONFIG_PATH, 5)
    assert not validator_test.is_path(CONFIG_PATH, 6)
    assert not validator_test.is_path(CONFIG_PATH, 10000)
    logger.info(">>> Verifying that the try counter allows a maximum number of attempts: PASSED")

