# 2023 BIO Question 1: Zeckendorf Representation


def fibonacci(n: int):
    nums = [1, 2]

    while nums[-1] < n:
        nums.append(nums[-1] + nums[-2])

    return nums


def solution(number: int) -> list[int]:
    representation = []

    for n in reversed(fibonacci(number)):
        if n <= number:
            number -= n
            representation.append(n)

    return representation


def main():
    print(" ".join([str(i) for i in solution(int(input()))]))


if __name__ == "__main__":
    main()
