import math

def is_prime(n):
    '''
    A simple function to determine if a number is prime.

    Input: 
        n (a number--cannot be a string)
    Output:
        True if n is prime
        False if n is not prime

    Example:
        is_prime(7): True
        is_prime(8): False
    '''
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True