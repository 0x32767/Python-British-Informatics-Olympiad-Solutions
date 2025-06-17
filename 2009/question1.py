# 2009 BIO Question 1: Digit Words


def check_case(word: str, digit: str):
    if len(word) <= len(digit):
        return word == digit

    digit_stk = list(digit)

    for letter in reversed(word):
        if letter == digit_stk[-1]:
            digit_stk.pop()

            if not len(digit_stk):
                return True

    return digit_stk == []


def solution(word: str):
    for idx, digit in enumerate(
        ("ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN"),
        start=1,
    ):
        if check_case(word, digit):
            return idx
    
    return "NO"

def main():
    print(solution(input()))

if __name__ == "__main__":
    main()
