import math


def get_primes(iterable: list):
    for i in iterable:
        is_prime = False
        if i > 1:
            is_prime = True
            for j in range(2, math.floor(i / 2) + 1):
                if i % j == 0:
                    is_prime = False
                    break
        if is_prime:
            yield i
