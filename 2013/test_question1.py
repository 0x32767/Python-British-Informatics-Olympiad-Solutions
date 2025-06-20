import unittest

from question1 import solution


class Test2013Question1(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(1, 31), "00:48")
        self.assertEqual(solution(0, 0), "01:00")
        self.assertEqual(solution(18, 18), "01:18")
        self.assertEqual(solution(67, 1507), "02:07")
        self.assertEqual(solution(0, 15), "00:00")
        self.assertEqual(solution(0, 7), "00:00")
        self.assertEqual(solution(17, 26), "13:20")
        self.assertEqual(solution(17, 215), "06:40")
        self.assertEqual(solution(5779, 5864), "19:12")
        self.assertEqual(solution(21923, 26268), "14:24")


if __name__ == "__main__":
    unittest.main()
