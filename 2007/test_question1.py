import unittest
from question1 import solution


class Test2007Question1(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(solution([3, 3, 3, 2, 10]), 6)
        self.assertEqual(solution([3, 4, 7, 9, 10]), 0)
        self.assertEqual(solution([7, 9, 2, 2, 10]), 1)
        self.assertEqual(solution([2, 7, 9, 10, 2]), 1)
        self.assertEqual(solution([2, 2, 3, 3, 4]), 2)
        self.assertEqual(solution([7, 6, 6, 6, 10]), 3)
        self.assertEqual(solution([1, 6, 2, 4, 9]), 2)
        self.assertEqual(solution([1, 8, 2, 3, 9]), 1)
        self.assertEqual(solution([2, 2, 7, 8, 2]), 4)
        self.assertEqual(solution([5, 5, 10, 5, 5]), 14)

if __name__ == "__main__":
    unittest.main()
