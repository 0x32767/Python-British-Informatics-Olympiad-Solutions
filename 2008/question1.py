# 2008 BIO Question 1: Goldbach Conjecture


def gen_primes(limit):
    primes = [2]

    for i in range(3, limit):
        for prime in primes:
            if i % prime == 0:
                break

        else:
            primes.append(i)

    return primes


def solution(target: int):
    primes = gen_primes(target - 1)
    combinations = 0

    for p in primes:
        complement = target - p

        if p > complement:
            break

        if complement in primes:
            combinations += 1

    return combinations

def main():
    target = int(input())
    print(solution(target))


if __name__ == "__main__":
    main()
