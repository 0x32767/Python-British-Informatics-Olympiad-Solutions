import unittest
from question1 import solution


class Test2006Question1(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(solution("OLYMPIAD", "OLYMPIAD"), "Anagrams")
        self.assertEqual(solution("LEMON", "MELON"), "Anagrams")
        self.assertEqual(solution("COVERSLIP", "SLIPCOVER"), "Anagrams")
        self.assertEqual(solution("TEARDROP", "PREDATOR"), "Anagrams")
        self.assertEqual(solution("ABBCCCDDD", "DDDCCCBBA"), "Anagrams")

        self.assertEqual(solution("I", "A"), "Not anagrams")
        self.assertEqual(solution("FORTY", "FORT"), "Not anagrams")
        self.assertEqual(solution("ONE", "SIX"), "Not anagrams")
        self.assertEqual(solution("GREEN", "RANGE"), "Not anagrams")
        self.assertEqual(solution("ABBCCCDDD", "AAABBBCCD"), "Not anagrams")

if __name__ == "__main__":
    unittest.main()
