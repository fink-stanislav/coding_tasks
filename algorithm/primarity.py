from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    
    primes = [2, 3, 5, 7]

    if n in primes:
        return True

    for prime in primes:
        if n % prime == 0:
            return False

    m = int(sqrt(n))
    
    if m % 2 == 0:
        m += 1

    for i in range(7, m + 1, 2):
        if n % i == 0:
            return False

    return True