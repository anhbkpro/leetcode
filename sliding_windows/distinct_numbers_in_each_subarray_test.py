import unittest
from .distinct_numbers_in_each_subarray import Solution, SolutionFrequencyArray


class BaseTestDistinctNumbers:
    """Base test class with common test cases"""
    def setUp(self):
        self.solution = self.SolutionClass()

    def test_basic_case(self):
        """Test with basic array with some repeating elements"""
        nums = [1, 2, 1, 3, 4]
        k = 3
        expected = [2, 3, 3]  # [1,2,1], [2,1,3], [1,3,4]
        self.assertEqual(self.solution.distinctNumbers(nums, k), expected)

    def test_all_unique(self):
        """Test with array containing all unique elements"""
        nums = [1, 2, 3, 4, 5]
        k = 2
        expected = [2, 2, 2, 2]  # [1,2], [2,3], [3,4], [4,5]
        self.assertEqual(self.solution.distinctNumbers(nums, k), expected)

    def test_all_same(self):
        """Test with array containing all same elements"""
        nums = [1, 1, 1, 1]
        k = 2
        expected = [1, 1, 1]  # [1,1], [1,1], [1,1]
        self.assertEqual(self.solution.distinctNumbers(nums, k), expected)

    def test_k_equals_array_length(self):
        """Test when k equals the array length"""
        nums = [1, 2, 3, 1]
        k = 4
        expected = [3]  # [1,2,3,1]
        self.assertEqual(self.solution.distinctNumbers(nums, k), expected)

    def test_k_equals_one(self):
        """Test when k equals 1"""
        nums = [1, 2, 1, 3]
        k = 1
        expected = [1, 1, 1, 1]  # [1], [2], [1], [3]
        self.assertEqual(self.solution.distinctNumbers(nums, k), expected)

    def test_mixed_numbers(self):
        """Test with mix of positive numbers"""
        nums = [1, 2, 1, 2, 1]
        k = 2
        expected = [2, 2, 2, 2]  # [1,2], [2,1], [1,2], [2,1]
        self.assertEqual(self.solution.distinctNumbers(nums, k), expected)


class TestDistinctNumbersHashMap(BaseTestDistinctNumbers, unittest.TestCase):
    """Test cases for the HashMap-based solution"""
    SolutionClass = Solution

    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-1, -2, -1, 1, 2]
        k = 3
        expected = [2, 3, 3]  # [-1,-2,-1], [-2,-1,1], [-1,1,2]
        self.assertEqual(self.solution.distinctNumbers(nums, k), expected)

    def test_large_numbers(self):
        """Test with large numbers"""
        nums = [1000000, 1000001, 1000000, 1000002]
        k = 2
        expected = [2, 2, 2]  # [1000000,1000001], [1000001,1000000], [1000000,1000002]
        self.assertEqual(self.solution.distinctNumbers(nums, k), expected)


class TestDistinctNumbersFrequencyArray(BaseTestDistinctNumbers, unittest.TestCase):
    """Test cases for the Frequency Array-based solution"""
    SolutionClass = SolutionFrequencyArray

    def test_small_range(self):
        """Test with small range of numbers"""
        nums = [0, 1, 0, 2, 1]
        k = 3
        expected = [2, 3, 3]  # [0,1,0], [1,0,2], [0,2,1]
        self.assertEqual(self.solution.distinctNumbers(nums, k), expected)

    def test_consecutive_numbers(self):
        """Test with consecutive numbers"""
        nums = [3, 4, 5, 3, 4]
        k = 2
        expected = [2, 2, 2, 2]  # [3,4], [4,5], [5,3], [3,4]
        self.assertEqual(self.solution.distinctNumbers(nums, k), expected)


if __name__ == "__main__":
    unittest.main()
