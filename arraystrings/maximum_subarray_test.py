import unittest
from .maximum_subarray import Solution


class TestMaximumSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        """Test with basic array containing both positive and negative numbers"""
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(self.solution.maxSubArray(nums), 6)  # Subarray [4,-1,2,1] has sum 6

    def test_single_element(self):
        """Test with single element array"""
        nums = [1]
        self.assertEqual(self.solution.maxSubArray(nums), 1)

    def test_all_negative(self):
        """Test with all negative numbers"""
        nums = [-2, -3, -1, -5]
        self.assertEqual(self.solution.maxSubArray(nums), -1)  # Single element [-1] is the maximum

    def test_all_positive(self):
        """Test with all positive numbers"""
        nums = [1, 2, 3, 4]
        self.assertEqual(self.solution.maxSubArray(nums), 10)  # Entire array is the maximum subarray

    def test_alternating_numbers(self):
        """Test with alternating positive and negative numbers"""
        nums = [1, -1, 2, -2, 3, -3]
        self.assertEqual(self.solution.maxSubArray(nums), 3)  # Single element [3] is the maximum

    def test_zero_elements(self):
        """Test with array containing zeros"""
        nums = [0, 0, -1, 0]
        self.assertEqual(self.solution.maxSubArray(nums), 0)  # Subarray [0] or [0,0] has sum 0

    def test_large_numbers(self):
        """Test with large numbers"""
        nums = [1000, -2000, 3000, -4000, 5000]
        self.assertEqual(self.solution.maxSubArray(nums), 5000)  # Single element [5000] is the maximum

    def test_multiple_equal_sums(self):
        """Test with multiple subarrays having equal sums"""
        nums = [1, -1, 1, -1, 1]
        self.assertEqual(self.solution.maxSubArray(nums), 1)  # Any single 1 is a maximum subarray


if __name__ == "__main__":
    unittest.main()
