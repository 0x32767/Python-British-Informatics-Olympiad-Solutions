import unittest
from question1 import solution


class Test2011Question1(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(solution("A", "A", 7), "M")
        self.assertEqual(solution("A", "M", 1), "A")
        self.assertEqual(solution("A", "A", 8), "U")
        self.assertEqual(solution("P", "Q", 101), "S")
        self.assertEqual(solution("Y", "Y", 1000), "U")
        self.assertEqual(solution("Z", "M", 5005), "Z")
        self.assertEqual(solution("K", "V", 10000), "C")
        self.assertEqual(solution("K", "Y", 20000), "W")
        self.assertEqual(solution("B", "I", 987654), "W")

if __name__ == "__main__":
    unittest.main()
