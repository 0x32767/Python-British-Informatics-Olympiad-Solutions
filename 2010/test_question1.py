import unittest
from question1 import solution


class Test2010Question1(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(solution(123456789), "2 4 5 7 8")
        self.assertEqual(solution(100), "NO")
        self.assertEqual(solution(1), "NO")
        self.assertEqual(solution(148258), "NO")
        self.assertEqual(solution(555), "NO")
        self.assertEqual(solution(1035), "3")
        self.assertEqual(solution(123876), "3 7")
        self.assertEqual(solution(142857), "2 3 4 5 6")
        self.assertEqual(solution(49271085), "2")
        self.assertEqual(solution(123450186), "7")

if __name__ == "__main__":
    unittest.main()
