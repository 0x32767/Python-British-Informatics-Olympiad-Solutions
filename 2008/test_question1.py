import unittest
from question1 import solution


class Test2008Question1(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(solution(22), 3)
        self.assertEqual(solution(4), 1)
        self.assertEqual(solution(8), 1)
        self.assertEqual(solution(62), 3)
        self.assertEqual(solution(114), 10)
        self.assertEqual(solution(346), 9)
        self.assertEqual(solution(1000), 28)
        self.assertEqual(solution(2326), 35)
        self.assertEqual(solution(5000), 76)
        self.assertEqual(solution(9240), 329)

if __name__ == "__main__":
    unittest.main()
