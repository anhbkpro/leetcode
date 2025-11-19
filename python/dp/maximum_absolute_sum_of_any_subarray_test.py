import unittest
from dp.maximum_absolute_sum_of_any_subarray import Solution


class TestMaximumAbsoluteSumOfAnySubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_and_negative_numbers(self):
        nums = [1, -3, 2, 3, -4]
        self.assertEqual(self.solution.maxAbsoluteSum(nums), 5)

    def test_all_positive_numbers(self):
        nums = [2, 3, 4, 1]
        self.assertEqual(self.solution.maxAbsoluteSum(nums), 10)

    def test_all_negative_numbers(self):
        nums = [-3, -2, -1]
        self.assertEqual(self.solution.maxAbsoluteSum(nums), 6)

    def test_single_element(self):
        nums = [5]
        self.assertEqual(self.solution.maxAbsoluteSum(nums), 5)

    def test_empty_array(self):
        nums = []
        self.assertEqual(self.solution.maxAbsoluteSum(nums), 0)

    def test_alternating_numbers(self):
        nums = [2, -5, 1, -4, 3, -2]
        self.assertEqual(self.solution.maxAbsoluteSum(nums), 8)

    def test_zero_sum_subarray(self):
        nums = [-1, 1, -1, 1]
        self.assertEqual(self.solution.maxAbsoluteSum(nums), 1)


if __name__ == "__main__":
    unittest.main()
