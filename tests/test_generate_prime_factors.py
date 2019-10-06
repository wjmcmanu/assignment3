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

def test_with_3():
    """ test_with_3 will return a list containing only the value 3"""
    assert 3 in prime.generate_prime_factors(3)

def test_with_4():
    """tet_with_4 will return a list containing a list with 2, specified twice"""
    assert prime.generate_prime_factors(4).count(2) == 2
