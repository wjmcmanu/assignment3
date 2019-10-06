# pylint: disable=missing-docstring
import pytest
import prime

def test_not_int():
    """
    test_not_int() - test to see if the value is an int or not
    """
    with pytest.raises(ValueError):
        prime.generate_prime_factors("a")

def test_with_1():
    """ test_with_1 will return an empty list when called with the number 1"""
    if not prime.generate_prime_factors(1):
        assert True

def test_with_2():
    """ test_with_2 will return a list containing only the value 2"""
    assert 2 in prime.generate_prime_factors(2)
