import unittest

from .longest_strictly_increasing_or_strictly_decreasing_subarray import Solution


class TestLongestMonotonicSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_strictly_increasing(self):
        """Test with strictly increasing sequence"""
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.longestMonotonicSubarray(nums), 5)

    def test_strictly_decreasing(self):
        """Test with strictly decreasing sequence"""
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.longestMonotonicSubarray(nums), 5)

    def test_mixed_sequence(self):
        """Test with mixed increasing and decreasing sequences"""
        nums = [1, 2, 3, 2, 1, 4, 5, 6]
        self.assertEqual(self.solution.longestMonotonicSubarray(nums), 4)

    def test_equal_elements(self):
        """Test with equal adjacent elements"""
        nums = [1, 2, 2, 3]
        self.assertEqual(self.solution.longestMonotonicSubarray(nums), 2)

    def test_single_element(self):
        """Test with single element array"""
        nums = [1]
        self.assertEqual(self.solution.longestMonotonicSubarray(nums), 1)

    def test_empty_array(self):
        """Test with empty array"""
        nums = []
        self.assertEqual(self.solution.longestMonotonicSubarray(nums), 1)

    def test_alternating_sequence(self):
        """Test with alternating increasing/decreasing sequence"""
        nums = [1, 3, 2, 4, 3, 5]
        self.assertEqual(self.solution.longestMonotonicSubarray(nums), 2)

    def test_all_equal_elements(self):
        """Test with all equal elements"""
        nums = [1, 1, 1, 1]
        self.assertEqual(self.solution.longestMonotonicSubarray(nums), 1)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-3, -2, -1, -4, -5]
        self.assertEqual(self.solution.longestMonotonicSubarray(nums), 3)


if __name__ == "__main__":
    unittest.main()
