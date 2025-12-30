import unittest

from sliding_windows.max_consecutive_ones import Solution


class TestMaxConsecutiveOnes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        nums = []
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 0)

    def test_all_ones(self):
        nums = [1, 1, 1, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 5)

    def test_all_zeros(self):
        nums = [0, 0, 0, 0, 0]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 0)

    def test_single_zero(self):
        nums = [1, 1, 0, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 2)

    def test_single_element_one(self):
        nums = [1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 1)

    def test_single_element_zero(self):
        nums = [0]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 0)

    def test_consecutive_zeros(self):
        nums = [1, 1, 0, 0, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 2)

    def test_complex_sequence(self):
        nums = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 3)
