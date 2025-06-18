# 2010 BIO Question 1: Anagram Numbers

from string import digits


def find_digit_frequency(num: int):
    return {d: str(num).count(d) for d in digits}


def solution(number: int):
    original_freq = find_digit_frequency(number)
    nums = []

    for i in range(2, 10):
        instance_freq = find_digit_frequency(number * i)

        if instance_freq == original_freq:
            nums.append(i)

    return " ".join([str(i) for i in nums]) or "NO"

def main():
    print(solution(int(input())))

if __name__ == "__main__":
    main()
