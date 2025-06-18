import unittest
from question1 import solution

from time import perf_counter_ns


class Timer:
    def __init__(self):
        self._start_time = 0
        self._time_elapsed = 0
        self.recorded_times = []

    @property
    def time_elapsed(self):
        # seconds
        return self._time_elapsed

    def __enter__(self):
        self._start_time = perf_counter_ns()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._time_elapsed = (perf_counter_ns() - self._start_time) / 1_000_000_000
        self.recorded_times.append(self.time_elapsed)


class Test2012Question1(unittest.TestCase):

    def test_solution(self):
        timer = Timer()
        
        with timer:
            self.assertEqual(solution(100), 10)

        with timer:
            self.assertEqual(solution(101), 101)

        with timer:
            self.assertEqual(solution(2), 2)

        with timer:
            self.assertEqual(solution(1001), 1001)

        with timer:
            self.assertEqual(solution(371293), 13)

        with timer:
            self.assertEqual(solution(789774), 789774)

        with timer:
            self.assertEqual(solution(999883), 999883)

        with timer:
            self.assertEqual(solution(561125), 335)

        with timer:
            self.assertEqual(solution(661229), 4379)

        # each run should have taken at most 3 seconds
        for time in timer.recorded_times:
            self.assertLess(time, 3)

if __name__ == "__main__":
    unittest.main()
