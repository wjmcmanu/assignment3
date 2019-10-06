"""
prime.py -- Write the application code here
"""
def generate_prime_factors(number):
    """
    Will accept an int and will return a list of ints
    """
    if not isinstance(number, int):
        raise ValueError
