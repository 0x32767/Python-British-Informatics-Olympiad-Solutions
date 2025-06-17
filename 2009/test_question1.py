import unittest
from question1 import solution


class Test2009Question1(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(solution("BOUNCE"), 1)
        self.assertEqual(solution("ENCODE"), "NO")
        self.assertEqual(solution("EIGHT"), 8)
        self.assertEqual(solution("BLACKJACK"), "NO")
        self.assertEqual(solution("FABULOUS"), "NO")
        self.assertEqual(solution("EXERCISE"), "NO")
        self.assertEqual(solution("DRIFTWOOD"), 2)
        self.assertEqual(solution("SERVICEMAN"), 7)
        self.assertEqual(solution("INSIGNIFICANCE"), 9)
        self.assertEqual(solution("THROWDOWN"), 2)

if __name__ == "__main__":
    unittest.main()
