# 2007 BIO Question 1: Cards

from math import comb
from itertools import permutations


def calc_repeated_points(nums: list[int]):
    # no repeated elements
    if len(set(nums)) == len(nums):
        return 0

    points = 0

    for n in set(nums):
        reps = nums.count(n)
        # comb returns how many ways k elements can be selected from n elements
        # if k < 2, comb(k, 2) = 0 so no checks needed
        points += comb(reps, 2)

    return points


def find_sum_15(numbers: list[int]):
    methods = set()

    get_value = lambda l: l[1]
    get_index = lambda l: l[0]

    # TODO make this better
    for last_n in range(2, len(numbers)):
        for permutation in permutations(enumerate(numbers), last_n):
            if sum(map(get_value, permutation)) == 15:
                methods.add(tuple(sorted(permutation, key=get_index)))

    return len(methods)


def solution(numbers: list[int]):
    return find_sum_15(numbers) + calc_repeated_points(numbers)

def main():
    numbers = input().split()
    nums = [int(n) for n in numbers]
    print(solution(nums))

if __name__ == "__main__":
    main()
