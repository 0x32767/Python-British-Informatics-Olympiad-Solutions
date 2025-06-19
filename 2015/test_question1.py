import unittest

from question1 import solution


class Test2015Question1(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution("BBACBB"), 3)
        self.assertEqual(solution("XX"), 1)
        self.assertEqual(solution("XY"), 0)
        self.assertEqual(solution("OLYMPIAD"), 0)
        self.assertEqual(solution("RACECAR"), 3)
        self.assertEqual(solution("KKKKKKK"), 7)
        self.assertEqual(solution("BBIIOIIBB"), 9)
        self.assertEqual(solution("PPPQQQQPPP"), 19)
        self.assertEqual(solution("AAAAAAAAAA"), 31)


if __name__ == "__main__":
    unittest.main()
