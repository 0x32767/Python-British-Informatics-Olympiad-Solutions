import unittest
from question1 import solution


class Test2017Question1(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(solution(list("R")), "R")
        self.assertEqual(solution(list("GG")), "G")
        self.assertEqual(solution(list("GR")), "B")
        self.assertEqual(solution(list("RRR")), "R")
        self.assertEqual(solution(list("RGB")), "G")
        self.assertEqual(solution(list("BGGRB")), "B")
        self.assertEqual(solution(list("BRGRBG")), "G")
        self.assertEqual(solution(list("GGGGGG")), "G")
        self.assertEqual(solution(list("GRBRBRBRBR")), "B")
        self.assertEqual(solution(list("RBGBGBGBGR")), "R")

if __name__ == "__main__":
    unittest.main()
