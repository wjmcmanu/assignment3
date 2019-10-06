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
    if number > 1:
        remainder = number
        divisor = 2
        while remainder != 1:
            if remainder % divisor == 0:
                list_of_ints.append(divisor)
                remainder = remainder / divisor
            else:
                divisor += 1
    return list_of_ints
