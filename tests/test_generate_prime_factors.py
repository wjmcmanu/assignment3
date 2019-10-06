# pylint: disable=missing-docstring
import pytest
import prime
"""
The test module for Prime Factors
"""
def test_not_int():
    """
    This will check to see if the value passed
    in is an int otherwise throw an Error
    """
    with pytest.raises(ValueError):
        prime.generate_prime_factors("a")
