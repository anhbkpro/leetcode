import unittest
from typing import List
import sys
import os

# Add the parent directory to the path to import the solution
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from longest_harmonious_subsequence import Solution


class TestLongestHarmoniousSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test Example 1: nums = [1,3,2,2,5,2,3,7]"""
        nums = [1, 3, 2, 2, 5, 2, 3, 7]
        expected = 5
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_example_2(self):
        """Test Example 2: nums = [1,2,3,4]"""
        nums = [1, 2, 3, 4]
        expected = 2
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_example_3(self):
        """Test Example 3: nums = [1,1,1,1]"""
        nums = [1, 1, 1, 1]
        expected = 0
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_single_element(self):
        """Test case with single element"""
        nums = [5]
        expected = 0
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_two_elements_same(self):
        """Test case with two identical elements"""
        nums = [3, 3]
        expected = 0
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_two_elements_consecutive(self):
        """Test case with two consecutive elements"""
        nums = [2, 3]
        expected = 2
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_two_elements_not_consecutive(self):
        """Test case with two elements that are not consecutive"""
        nums = [1, 5]
        expected = 0
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_three_elements_consecutive(self):
        """Test case with three consecutive elements"""
        nums = [1, 2, 3]
        expected = 2
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_multiple_consecutive_pairs(self):
        """Test case with multiple consecutive pairs"""
        nums = [1, 2, 3, 4, 5]
        expected = 2
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_duplicates_with_consecutive(self):
        """Test case with duplicates and consecutive elements"""
        nums = [1, 1, 2, 2, 3, 3]
        expected = 4
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_negative_numbers(self):
        """Test case with negative numbers"""
        nums = [-2, -1, 0, 1, 2]
        expected = 2
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_mixed_negative_positive(self):
        """Test case with mixed negative and positive numbers"""
        nums = [-1, 0, 1, 2, 3]
        expected = 2
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_large_numbers(self):
        """Test case with large numbers"""
        nums = [1000000, 1000001, 1000002]
        expected = 2
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_very_large_numbers(self):
        """Test case with very large numbers"""
        nums = [10**9, 10**9 + 1]
        expected = 2
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_very_small_numbers(self):
        """Test case with very small numbers"""
        nums = [-(10**9), -(10**9) + 1]
        expected = 2
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_complex_case_1(self):
        """Test a complex case with multiple harmonious subsequences"""
        nums = [1, 2, 2, 3, 3, 3, 4, 4, 5]
        expected = 5  # [2,2,3,3,3] or similar
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_complex_case_2(self):
        """Test another complex case"""
        nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
        expected = 6  # [1,1,1,2,2,2] or similar
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_no_harmonious_subsequence(self):
        """Test case with no harmonious subsequence"""
        nums = [1, 3, 5, 7, 9]
        expected = 0
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_all_zeros(self):
        """Test case with all zeros"""
        nums = [0, 0, 0, 0]
        expected = 0
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_zeros_and_ones(self):
        """Test case with zeros and ones"""
        nums = [0, 0, 1, 1, 1]
        expected = 5
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_sparse_array(self):
        """Test case with sparse array (large gaps)"""
        nums = [1, 10, 20, 30, 40]
        expected = 0
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_alternating_consecutive(self):
        """Test case with alternating consecutive numbers"""
        nums = [1, 2, 4, 5, 7, 8]
        expected = 2  # [1,2,4,5,7,8]
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_edge_case_minimum_length(self):
        """Test case with minimum length array"""
        nums = [1]
        expected = 0
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_edge_case_maximum_length(self):
        """Test case with maximum length array (all same elements)"""
        nums = [5] * 20000
        expected = 0
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_edge_case_maximum_length_consecutive(self):
        """Test case with maximum length array (consecutive elements)"""
        nums = list(range(10000, 20000))
        expected = 2
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_multiple_harmonious_ranges(self):
        """Test case with multiple harmonious ranges"""
        nums = [1, 2, 3, 5, 6, 7, 9, 10, 11]
        expected = 2
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_disjoint_harmonious_ranges(self):
        """Test case with disjoint harmonious ranges"""
        nums = [1, 2, 3, 5, 6, 7, 10, 11, 12]
        expected = 2
        result = self.solution.findLHS(nums)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")


if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)
