def solution(n: int):
    # last 5 tests take too long
    # TODO make blazingly fast, use strings instead of ints
    n += 1

    while list(str(n)) != list(reversed(str(n))):
        n += 1

    return n

def main():
    print(solution(int(input())))


if __name__ == "__main__":
    main()
