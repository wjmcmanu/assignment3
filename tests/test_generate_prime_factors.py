# pylint: disable=missing-docstring
import pytest
import prime

def test_not_int():
    """
    test_not_int() - test to see if the value is an int or not
    """
    with pytest.raises(ValueError):
        prime.generate_prime_factors("a")
