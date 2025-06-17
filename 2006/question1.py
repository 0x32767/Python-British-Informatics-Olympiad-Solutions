# 2006 BIO Question 1: Anagrams


def solution(word_1: str, word_2: str):
    freq_1 = {letter: word_1.count(letter) for letter in word_1}
    freq_2 = {letter: word_2.count(letter) for letter in word_2}

    if freq_1 == freq_2:
        return "Anagrams"

    else:
        return "Not anagrams"

def main():
    word_1 = input()
    word_2 = input()

    print(solution(word_1, word_2))

if __name__ == "__main__":
    main()
