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


@pytest.mark.validator
def test_to_validate_empty_values():
    """
    Verifying that the empty values not be allowed
    """
    no_empty_value = "asdf"
    validator_test = Validator()

    assert validator_test.empty_validation(str(no_empty_value))
    logger.info(">>> Verifying that the empty values not be allowed: PASSED")


@pytest.mark.validator
def test_is_text():
    """
    Verify that the text values are validated
    """
    text_value = "asdfg"
    float_value = "0.5"
    empty_value = None
    int_value = 10

    validator_test = Validator()

    assert not validator_test.is_only_text(str(text_value))
    assert not validator_test.is_only_text(float_value)
    assert not validator_test.is_only_text(empty_value)
    assert validator_test.is_only_text(int_value)
    logger.info(">>> Verifying that the text values are validated: PASSED")


@pytest.mark.validator
def test_it_is_not_file():
    """
    Verifying that it is not file
    """
    path = CONFIG_PATH + "\somethingxt888"

    validator_test = Validator()
    assert not validator_test.is_file(path)
    logger.info(">>> Verifying that it is not file: PASSED")

