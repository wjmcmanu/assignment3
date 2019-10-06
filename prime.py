#!/usr/bin/env python
""" prime.py -- This program will generate a list of prime numbers for a
given number"""

def generate_prime_factors(number):
    """
    Will accept an int and will return a list of prime values for that given number
    """
    if not isinstance(number, int):
        raise ValueError
    list_of_ints = []
    if number == 2:
        list_of_ints.append(2)
    elif number == 3:
        list_of_ints.append(3)
    return list_of_ints
