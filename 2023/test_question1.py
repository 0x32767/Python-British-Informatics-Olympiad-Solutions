import unittest
from question1 import solution


class Test2007Question1(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(sorted(solution(100)), [3, 8, 89])
        self.assertEqual(sorted(solution(1)), [1])
        self.assertEqual(sorted(solution(832040)), [832040])
        self.assertEqual(sorted(solution(4)), [1, 3])
        self.assertEqual(sorted(solution(623)), [13, 610])
        self.assertEqual(sorted(solution(12)), [1, 3, 8])
        self.assertEqual(sorted(solution(834629)), [5, 2584, 832040])
        self.assertEqual(sorted(solution(33)), [1, 3, 8, 21])
        self.assertEqual(sorted(solution(2023)), [2, 13, 34, 377, 1597])
        self.assertEqual(sorted(solution(5000)), [2, 8, 55, 144, 610, 4181])
        self.assertEqual(sorted(solution(514228)), [1, 3, 8, 21, 55, 144, 377, 987, 2584, 6765, 17711, 46368, 121393, 317811])

if __name__ == "__main__":
    unittest.main()
