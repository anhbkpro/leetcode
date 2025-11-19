import pytest
from .minimum_operations_to_make_binary_array_elements_equal_to_one_i import Solution


class TestMinOperations:
    def setup_method(self):
        self.solution = Solution()

    def test_empty_array(self):
        """Test case with empty array"""
        assert self.solution.minOperations([]) == 0

    def test_single_element(self):
        """Test case with single element"""
        assert self.solution.minOperations([1]) == 0
        assert self.solution.minOperations([0]) == -1

    def test_all_ones(self):
        """Test case where array contains all ones"""
        assert self.solution.minOperations([1, 1, 1, 1]) == 0
        assert self.solution.minOperations([1, 1]) == 0

    def test_simple_convertible(self):
        """Test case with simple convertible arrays"""
        assert self.solution.minOperations([0, 1, 1]) == -1
        assert self.solution.minOperations([1, 0, 1]) == -1
        assert self.solution.minOperations([1, 1, 0]) == -1

    def test_multiple_operations(self):
        """Test case requiring multiple operations"""
        assert self.solution.minOperations([0, 0, 0, 1, 1, 1]) == 1
        assert self.solution.minOperations([1, 0, 0, 0, 1, 1]) == 1

    def test_impossible_cases(self):
        """Test cases where conversion is impossible"""
        assert self.solution.minOperations([0, 0]) == -1
        assert self.solution.minOperations([1, 1, 0, 0]) == -1

    def test_alternating_pattern(self):
        """Test case with alternating pattern"""
        assert self.solution.minOperations([1, 0, 1, 0, 1]) == -1
        assert self.solution.minOperations([0, 1, 0, 1, 0]) == 3

    def test_edge_cases(self):
        """Test edge cases"""
        assert self.solution.minOperations([0, 1, 0]) == -1
        assert self.solution.minOperations([1, 0, 0, 1]) == -1
        assert self.solution.minOperations([0, 0, 1, 1, 1]) == -1

    def test_leetcode_examples(self):
        """Test the examples from LeetCode"""
        assert self.solution.minOperations([0, 1, 1, 1, 0, 0]) == 3
        assert self.solution.minOperations([1, 1, 1]) == 0
        assert self.solution.minOperations([1, 1, 0]) == -1
        assert self.solution.minOperations([0, 0, 0, 1]) == 1
