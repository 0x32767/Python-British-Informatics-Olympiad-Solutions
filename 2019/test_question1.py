import unittest

from question1 import solution


class Test2019Question1(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(solution(5), 6)
        self.assertEqual(solution(9), 11)
        self.assertEqual(solution(33), 44)
        self.assertEqual(solution(84), 88)
        self.assertEqual(solution(45653), 45654)
        self.assertEqual(solution(36460000), 36466463)
        self.assertEqual(solution(24355343), 24366342)
        self.assertEqual(solution(123450000), 123454321)
        self.assertEqual(solution(234567890), 234575432)
        self.assertEqual(solution(678999876), 679000976)
        self.assertEqual(solution(99999999999999), 100000000000001)
        self.assertEqual(solution(999999999999999), 1000000000000001)
        
        self.assertEqual(solution(123456789000000000), 123456789987654321)
        self.assertEqual(solution(987654321123456789), 987654322223456789)
        self.assertEqual(solution(1234567890000000000), 1234567890987654321)
        self.assertEqual(solution(9876543210123456789), 9876543211123456789)
        self.assertEqual(solution(9876543219123456789), 9876543220223456789)

if __name__ == "__main__":
    unittest.main()
