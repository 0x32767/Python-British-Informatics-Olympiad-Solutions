# 2011 BIO Question 1: Fibonacci letters

from string import ascii_uppercase as orig_ascii_uppercase


def solution(term_1: str, term_2: str, itr: int):
    ascii_uppercase = "_" + orig_ascii_uppercase

    if itr == 1:
        return term_1

    elif itr == 2:
        return term_2

    lst = [term_1, term_2]

    while len(lst) < int(itr):
        last2 = ascii_uppercase.index(lst[-2])
        last = ascii_uppercase.index(lst[-1])
        lst.append(ascii_uppercase[(last + last2) % 26 or 26])

    return lst[-1]


def main():
    term_1, term_2, itr = input().split()
    print(solution(term_1, term_2, int(itr)))

if __name__ == "__main__":
    main()
