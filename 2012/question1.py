# 2012 BIO Question 1: Distinct Prime Factorisation

from math import sqrt


def factorize(target: int):
    primes = [2]

    for possible_prime in range(2, target + 1):
        # prime detection
        is_prime = True
        for prime in primes:
            # small optimization to improve efficiency
            if prime > sqrt(possible_prime):
                break

            if possible_prime % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(possible_prime)

    return {prime for prime in primes if target % prime == 0}


def solution(number: int):
    res = 1

    for i in factorize(number):
        res *= i

    return res

def main():
    print(solution(int(input())))

if __name__ == "__main__":
    main()
