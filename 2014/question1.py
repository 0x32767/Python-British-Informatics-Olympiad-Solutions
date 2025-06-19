# 2014 BIO Question 1: Lucky Numbers

def generate_lucky_numbers():
    # 10,004 is the first lucky number over 10k
    nums = list(range(1, 10_004, 2))
    last_lucky = 3

    for _ in range(168):
        for i in reversed(range(last_lucky-1, len(nums), last_lucky)):
            del nums[i]

        for i in nums:
            if i > last_lucky:
                last_lucky = i
                break

    return nums

def solution(number: int) -> str:
    last = 1
    numbers = generate_lucky_numbers()

    for idx_next, lucky in enumerate(numbers, start=1):
        if lucky > number:
            return f"{last} {lucky}"
    
        elif lucky == number:
            return f"{last} {numbers[idx_next]}"

        last = lucky

def main():
    number = int(input())
    print(solution(number))

if __name__ == "__main__":
    main()
