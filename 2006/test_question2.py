import unittest
from question2 import solution


class Test2006Question2(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(solution("x", "7", "12"), ("Yes", "No"))
        self.assertEqual(solution("xux", "667", "65"), ("No", "No"))
        self.assertEqual(solution("xddu", "8654", "2102"), ("No", "Yes"))
        self.assertEqual(solution("xuxd", "9801", "4543"), ("No", "Yes"))
        self.assertEqual(solution("xx*", "0", "2006"), ("Yes", "Yes"))
        self.assertEqual(solution("xd*u?", "56", "54322"), ("Yes", "No"))
        self.assertEqual(solution("x?x", "1", "11"), ("Yes", "Yes"))
        self.assertEqual(solution("x?x", "123", "4567"), ("No", "No"))
        self.assertEqual(solution("x*xu", "7654", "2"), ("No", "No"))
        self.assertEqual(solution("x(xud)?", "789", "7890"), ("No", "Yes"))
        self.assertEqual(solution("x(xd)?(xu)?", "421", "422"), ("Yes", "No"))
        self.assertEqual(solution("x(ud)*u?", "0836", "19181716151"), ("Yes", "Yes"))

if __name__ == "__main__":
    unittest.main()
