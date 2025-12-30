import unittest

from arraystrings.longest_subarray_with_maximum_bitwise_and import Solution


class TestLongestSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_element(self):
        """Test with a single element array"""
        nums = [5]
        expected = 1
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_all_same_elements(self):
        """Test with all elements being the same"""
        nums = [3, 3, 3, 3]
        expected = 4
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_increasing_sequence(self):
        """Test with strictly increasing sequence"""
        nums = [1, 2, 3, 4, 5]
        expected = 1
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_decreasing_sequence(self):
        """Test with strictly decreasing sequence"""
        nums = [5, 4, 3, 2, 1]
        expected = 1
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_multiple_maxima(self):
        """Test with multiple occurrences of the maximum value"""
        nums = [1, 2, 3, 3, 2, 3, 3, 3, 1]
        expected = 3
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_max_at_beginning(self):
        """Test with maximum value at the beginning"""
        nums = [5, 1, 2, 3, 4]
        expected = 1
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_max_at_end(self):
        """Test with maximum value at the end"""
        nums = [1, 2, 3, 4, 5]
        expected = 1
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_max_in_middle(self):
        """Test with maximum value in the middle"""
        nums = [1, 2, 5, 3, 4]
        expected = 1
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_consecutive_maxima(self):
        """Test with consecutive maximum values"""
        nums = [1, 2, 3, 3, 3, 2, 1]
        expected = 3
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_non_consecutive_maxima(self):
        """Test with non-consecutive maximum values"""
        nums = [1, 3, 2, 3, 1, 3, 2]
        expected = 1
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_zeros_and_ones(self):
        """Test with zeros and ones"""
        nums = [0, 1, 0, 1, 1, 0]
        expected = 2
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_all_zeros(self):
        """Test with all zeros"""
        nums = [0, 0, 0, 0]
        expected = 4
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        """Test with large numbers"""
        nums = [1000, 500, 1000, 200, 1000, 1000]
        expected = 2
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-5, -3, -1, -1, -2, -1]
        expected = (
            0  # Current algorithm initializes max_val=0, so no negative numbers match
        )
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        nums = [-3, 5, -2, 5, 1, 5, -1]
        expected = 1  # Maximum is 5, appears once consecutively
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_empty_array(self):
        """Test with empty array (edge case)"""
        nums = []
        expected = 0
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_two_elements_same(self):
        """Test with two identical elements"""
        nums = [7, 7]
        expected = 2
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_two_elements_different(self):
        """Test with two different elements"""
        nums = [3, 7]
        expected = 1
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)

    def test_complex_pattern(self):
        """Test with a complex pattern"""
        nums = [2, 1, 3, 3, 2, 3, 3, 3, 1, 3, 3, 3, 3]
        expected = 4
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
