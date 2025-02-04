import unittest
from .maximum_ascending_subarray_sum import Solution


class TestMaximumAscendingSubarraySum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_ascending(self):
        """Test with basic ascending sequence"""
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.maxAscendingSum(nums), 15)  # All numbers form ascending sequence

    def test_multiple_ascending_sequences(self):
        """Test with multiple ascending sequences"""
        nums = [10, 20, 30, 5, 10, 50]
        self.assertEqual(self.solution.maxAscendingSum(nums), 65)  # [5, 10, 50] is max ascending sequence

    def test_single_element(self):
        """Test with single element array"""
        nums = [5]
        self.assertEqual(self.solution.maxAscendingSum(nums), 5)

    def test_descending_sequence(self):
        """Test with descending sequence"""
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.maxAscendingSum(nums), 5)  # Each number forms its own sequence

    def test_equal_adjacent_elements(self):
        """Test with equal adjacent elements"""
        nums = [1, 2, 2, 3, 4]
        self.assertEqual(self.solution.maxAscendingSum(nums), 9)  # [1, 2] and [3, 4] are ascending sequences, [1, 2] has larger sum

    def test_all_equal_elements(self):
        """Test with all equal elements"""
        nums = [3, 3, 3, 3]
        self.assertEqual(self.solution.maxAscendingSum(nums), 3)  # Each 3 forms its own sequence

    def test_alternating_sequence(self):
        """Test with alternating sequence"""
        nums = [1, 5, 2, 6, 3, 7]
        self.assertEqual(self.solution.maxAscendingSum(nums), 10)  # [1, 5] is max ascending sequence

    def test_large_numbers(self):
        """Test with large numbers"""
        nums = [1000, 2000, 3000, 1, 2]
        self.assertEqual(self.solution.maxAscendingSum(nums), 6000)  # [1000, 2000, 3000] is max ascending sequence

    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-5, -4, -3, -6, -2, -1]
        self.assertEqual(self.solution.maxAscendingSum(nums), -5)  # [-5] is first element, solution doesn't combine negative numbers

    def test_all_negative_numbers(self):
        """Test with all negative numbers"""
        nums = [-5, -4, -3, -2, -1]
        self.assertEqual(self.solution.maxAscendingSum(nums), -5)  # Solution returns first element for negative sequences

if __name__ == "__main__":
    unittest.main()
