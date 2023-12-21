from prime2_clp2181 import prime2_clp2181

## a) Write a test function test_is_prime that checks the is_prime function using a set of known prime numbers (e.g., 2, 7) and composite numbers (e.g. 8, 9)##
def test_is_prime():
    assert prime2_clp2181.is_prime(2) is True #testing if is_prime function correctly identifies 2 and 7 as prime, and 8 and 9 as not prime
    assert prime2_clp2181.is_prime(7) is True 
    assert prime2_clp2181.is_prime(8) is False
    assert prime2_clp2181.is_prime(9) is False
    
## b) Parameterize a test function test_is_prime_param to check the is_prime function with various numbers of primes and composite numbers, including edge cases such as negative numbers, 0, and 1. ##
def test_is_prime_param():
    for n in [2, 3, 5, 7, 11, 13]: #testing if is_prime function correctly identifies list as prime
        assert prime2_clp2181.is_prime(n) is True 
    for n in [-1, 0, 1, 4, 6, 8,]: ##testing if is_prime function correctly identifies list as not prime
        assert prime2_clp2181.is_prime(n) is False