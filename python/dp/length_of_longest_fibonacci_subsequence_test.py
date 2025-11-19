import unittest
from dp.length_of_longest_fibonacci_subsequence import (
    Solution,
    SolutionDP,
    SolutionOptimizedDP,
)


class TestLengthOfLongestFibonacciSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution_dp = SolutionDP()
        self.solution_optimized = SolutionOptimizedDP()

    def test_basic_fibonacci_sequence(self):
        arr = [1, 2, 3, 5, 8]
        expected = 5
        self.assertEqual(self.solution.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_dp.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_optimized.lenLongestFibSubseq(arr), expected)

    def test_multiple_fibonacci_sequences(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = 5  # [1,2,3,5,8] or [2,3,5,8]
        self.assertEqual(self.solution.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_dp.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_optimized.lenLongestFibSubseq(arr), expected)

    def test_no_fibonacci_sequence(self):
        arr = [1, 3, 7, 11, 12, 14, 18]
        expected = 3  # [3,7,11] forms a valid Fibonacci sequence
        self.assertEqual(self.solution.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_dp.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_optimized.lenLongestFibSubseq(arr), expected)

    def test_minimal_fibonacci_sequence(self):
        arr = [1, 2, 3]
        expected = 3
        self.assertEqual(self.solution.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_dp.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_optimized.lenLongestFibSubseq(arr), expected)

    def test_array_too_short(self):
        arr = [1, 2]
        expected = 0
        self.assertEqual(self.solution.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_dp.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_optimized.lenLongestFibSubseq(arr), expected)

    def test_large_numbers(self):
        arr = [2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]
        expected = 5  # [2,8,10,18,23] forms a valid Fibonacci sequence
        self.assertEqual(self.solution.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_dp.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_optimized.lenLongestFibSubseq(arr), expected)

    def test_overlapping_sequences(self):
        arr = [1, 3, 4, 7, 11, 18, 29]
        expected = 7  # [1,3,4,7,11,18,29] forms a valid Fibonacci sequence
        self.assertEqual(self.solution.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_dp.lenLongestFibSubseq(arr), expected)
        self.assertEqual(self.solution_optimized.lenLongestFibSubseq(arr), expected)


if __name__ == "__main__":
    unittest.main()
