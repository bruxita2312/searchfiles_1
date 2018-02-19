"""class for unit tests"""

import pytest
from src.com.jalasoft.search_files.validator.validator import Validator

@pytest.mark.validator
def test_a_validator_is_created_without_parameters():
    """
    testing that validator object is being created
     :return:
    """
    validator_test = Validator()
    assert isinstance(validator_test, Validator)


