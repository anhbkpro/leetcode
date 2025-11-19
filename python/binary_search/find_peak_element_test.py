import unittest
from .find_peak_element import Solution


class TestFindPeakElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_peak(self):
        """Test with array having obvious peak in middle"""
        nums = [1, 2, 3, 1]
        result = self.solution.findPeakElement(nums)
        self.assertEqual(nums[result], 3)
        self.assertTrue(result == 2)

    def test_multiple_peaks(self):
        """Test array with multiple peaks - should return any valid peak"""
        nums = [1, 3, 2, 4, 1]
        result = self.solution.findPeakElement(nums)
        # Check if returned index is actually a peak
        if result > 0:
            self.assertTrue(nums[result] > nums[result - 1])
        if result < len(nums) - 1:
            self.assertTrue(nums[result] > nums[result + 1])

    def test_strictly_increasing(self):
        """Test with strictly increasing array"""
        nums = [1, 2, 3, 4, 5]
        result = self.solution.findPeakElement(nums)
        self.assertEqual(result, 4)  # Last element should be peak

    def test_strictly_decreasing(self):
        """Test with strictly decreasing array"""
        nums = [5, 4, 3, 2, 1]
        result = self.solution.findPeakElement(nums)
        self.assertEqual(result, 0)  # First element should be peak

    def test_single_element(self):
        """Test array with single element"""
        nums = [1]
        self.assertEqual(self.solution.findPeakElement(nums), 0)

    def test_two_elements(self):
        """Test array with two elements"""
        # Increasing
        nums = [1, 2]
        self.assertEqual(self.solution.findPeakElement(nums), 1)

        # Decreasing
        nums = [2, 1]
        self.assertEqual(self.solution.findPeakElement(nums), 0)

    def test_alternating_elements(self):
        """Test with alternating high and low elements"""
        nums = [1, 3, 1, 4, 1, 2, 1]
        result = self.solution.findPeakElement(nums)
        # Verify the result is a peak
        if result > 0:
            self.assertTrue(nums[result] > nums[result - 1])
        if result < len(nums) - 1:
            self.assertTrue(nums[result] > nums[result + 1])

    def test_plateau_not_peak(self):
        """Test with plateau (equal adjacent elements) is considered"""
        nums = [1, 2, 2, 2, 1]
        result = self.solution.findPeakElement(nums)
        # The result should be at any of the equal elements
        self.assertEqual(nums[result], 2)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-3, -2, -5, -1]
        result = self.solution.findPeakElement(nums)
        self.assertEqual(result, 1)  # -2 is a peak

    def test_edge_cases(self):
        """Test edge cases with minimum and maximum integers"""
        nums = [float("-inf"), 1, float("-inf")]
        self.assertEqual(self.solution.findPeakElement(nums), 1)


if __name__ == "__main__":
    unittest.main()
