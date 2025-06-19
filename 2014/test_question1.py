import unittest

from question1 import solution


class Test2014Question1(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(5), "3 7")
        self.assertEqual(solution(33), "31 37")
        self.assertEqual(solution(34), "33 37")
        self.assertEqual(solution(399), "393 409")
        self.assertEqual(solution(456), "451 463")
        self.assertEqual(solution(3301), "3297 3307")
        self.assertEqual(solution(3304), "3301 3307")
        self.assertEqual(solution(9703), "9691 9727")
        self.assertEqual(solution(10000), "9999 10003")


if __name__ == "__main__":
    unittest.main()
