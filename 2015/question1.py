# 2015 BIO Question 1: Block Palindromes

def solution(string: str):
    methods = 0

    for n in range(1, len(string)//2 + 1):
        first_n = string[:n]
        last_n = string[-n:]
        middle = string[n:-n]

        if first_n == last_n:
            # methods.append((first_n, middle, last_n))
            # methods.extend((first_n, *m, last_n) for m in solution(middle))
            methods += 1 + solution(middle)

    return methods

def main():
    word = input()
    print(solution(word))

if __name__ == "__main__":
    main()
