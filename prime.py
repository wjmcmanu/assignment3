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
        if number == 3:
            list_of_ints.append(3)
        else:
            running_total = 2
            while running_total <= number:
                list_of_ints.append(2)
                running_total = running_total * 2
    return list_of_ints
