# Find the largest prime factor of 600851475143
import math


def is_prime(n):
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

def sieve_of_eratosthenes(num: int):
    is_prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:
        if is_prime[p]:
            for i in range(p*p, num+1, p):
                is_prime[i] = False
        p += 1

    prime_nums = []
    for i, p in enumerate(is_prime):
        if p:
            prime_nums.append(i)
    return prime_nums


# def largest_prime_factor(primes: [], num: int):
#     for prime in reversed(primes):
#         if num % prime == 0:
#             return prime


def largest_prime_factor(n):
    factors = []
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if is_prime(x):
            if n % x == 0:
                pair = n / x
                factors.append(x)
                if is_prime(pair):
                    factors.append(pair)
    return sorted(factors)[-1]


if __name__ == '__main__':
    num = 600851475143
    # num = 13195
    print(largest_prime_factor(num))
