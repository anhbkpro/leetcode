import unittest
from typing import List
import sys
import os

# Add the parent directory to the path to import the solution
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from find_subsequence_of_length_k_with_the_largest_sum import Solution


class TestMaxSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test Example 1: nums = [2,1,3,3], k = 2"""
        nums = [2, 1, 3, 3]
        k = 2
        expected = [3, 3]  # The two largest elements are 3 and 3
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_example_2(self):
        """Test Example 2: nums = [-1,-2,3,4], k = 3"""
        nums = [-1, -2, 3, 4]
        k = 3
        expected = [-1, 3, 4]  # The three largest elements in order
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_example_3(self):
        """Test Example 3: nums = [3,4,3,3], k = 2"""
        nums = [3, 4, 3, 3]
        k = 2
        expected = [3, 4]  # The two largest elements in order
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_all_positive_numbers(self):
        """Test case with all positive numbers"""
        nums = [5, 2, 8, 1, 9, 3]
        k = 3
        expected = [5, 8, 9]  # The three largest elements in order
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_all_negative_numbers(self):
        """Test case with all negative numbers"""
        nums = [-5, -2, -8, -1, -9, -3]
        k = 3
        expected = [-2, -1, -3]  # The three largest (least negative) elements in order
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_mixed_positive_negative(self):
        """Test case with mixed positive and negative numbers"""
        nums = [1, -5, 3, -2, 7, -1]
        k = 4
        expected = [1, 3, 7, -1]  # The four largest elements in order
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_duplicate_elements(self):
        """Test case with duplicate elements"""
        nums = [2, 2, 2, 1, 1, 1]
        k = 4
        expected = [2, 2, 2, 1]  # Four largest elements in order
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_k_equals_length(self):
        """Test case where k equals the length of the array"""
        nums = [1, 2, 3, 4, 5]
        k = 5
        expected = [1, 2, 3, 4, 5]  # All elements in original order
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_k_equals_one(self):
        """Test case where k equals 1"""
        nums = [5, 2, 8, 1, 9, 3]
        k = 1
        expected = [9]  # The largest element
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_single_element_array(self):
        """Test case with single element array"""
        nums = [42]
        k = 1
        expected = [42]
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_zeros_in_array(self):
        """Test case with zeros in the array"""
        nums = [0, 1, 0, 2, 0, 3]
        k = 3
        expected = [1, 2, 3]  # The three largest non-zero elements in order
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_large_numbers(self):
        """Test case with large numbers"""
        nums = [1000000, 999999, 1000001, 999998]
        k = 2
        expected = [1000000, 1000001]  # The two largest elements in order
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_negative_k_edge_case(self):
        """Test case with k = 0 (edge case)"""
        nums = [1, 2, 3, 4, 5]
        k = 0
        expected = []  # Empty subsequence
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_identical_elements(self):
        """Test case with all identical elements"""
        nums = [7, 7, 7, 7, 7]
        k = 3
        expected = [7, 7, 7]  # Any three elements in order
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_decreasing_order(self):
        """Test case with elements in decreasing order"""
        nums = [5, 4, 3, 2, 1]
        k = 3
        expected = [5, 4, 3]  # First three elements
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_increasing_order(self):
        """Test case with elements in increasing order"""
        nums = [1, 2, 3, 4, 5]
        k = 3
        expected = [3, 4, 5]  # Last three elements
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_complex_case(self):
        """Test a more complex case"""
        nums = [10, 2, 8, 5, 1, 9, 3, 7, 4, 6]
        k = 5
        expected = [10, 8, 9, 7, 6]  # The five largest elements in order
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_preserve_order_importance(self):
        """Test that order is preserved correctly"""
        nums = [3, 1, 2, 4, 5]
        k = 3
        expected = [3, 4, 5]  # Should preserve the order of 3, 4, 5
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_edge_case_empty_array(self):
        """Test case with empty array"""
        nums = []
        k = 0
        expected = []
        result = self.solution.maxSubsequence(nums, k)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")


if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)
