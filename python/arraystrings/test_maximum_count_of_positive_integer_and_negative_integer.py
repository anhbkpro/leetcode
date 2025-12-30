import pytest

from .maximum_count_of_positive_integer_and_negative_integer import (
    BinarySearchSolution,
    OnePassSolution,
    Solution,
)


@pytest.fixture
def solution():
    return Solution()


@pytest.fixture
def one_pass_solution():
    return OnePassSolution()


@pytest.fixture
def binary_search_solution():
    return BinarySearchSolution()


def test_basic_functionality(solution, binary_search_solution):
    test_cases = [
        ([-2, -1, -1, 1, 2, 3], 3),
        ([-3, -2, -1, 0, 0, 1, 2], 3),
        ([1, 2, 3, 4, 5], 5),
    ]
    for nums, expected in test_cases:
        assert solution.maximumCount(nums) == expected
        assert binary_search_solution.maximumCount(nums) == expected


def test_edge_cases(solution, binary_search_solution):
    test_cases = [
        ([], 0),  # Empty array
        ([0, 0, 0], 0),  # Array with only zeros
        ([1], 1),  # Single positive
        ([-1], 1),  # Single negative
        ([0], 0),  # Single zero
    ]
    for nums, expected in test_cases:
        assert solution.maximumCount(nums) == expected
        assert binary_search_solution.maximumCount(nums) == expected


def test_special_cases(solution, binary_search_solution):
    test_cases = [
        ([-3, -2, -1], 3),  # All negative
        ([1, 2, 3], 3),  # All positive
        ([-1, 0, 0, 0, 0, 1], 1),  # More zeros
        ([-2, -1, 1, 2], 2),  # Equal positives/negatives
    ]
    for nums, expected in test_cases:
        assert solution.maximumCount(nums) == expected
        assert binary_search_solution.maximumCount(nums) == expected


def test_input_variations(solution, binary_search_solution):
    test_cases = [
        ([-1000000, 1000000], 1),  # Large numbers
        ([-2, -1, 0, 1, 2], 2),  # Consecutive
        ([-2, -2, 1, 1, 1], 3),  # Duplicates
        ([2, -1, 0, 1, -2], 2),  # Mixed order
    ]
    for nums, expected in test_cases:
        assert solution.maximumCount(nums) == expected
        assert binary_search_solution.maximumCount(nums) == expected


def test_binary_search_specific(binary_search_solution):
    """Test cases specifically designed for binary search edge cases"""
    test_cases = [
        ([0] * 1000 + [1], 1),  # Many zeros before positive
        ([-1] + [0] * 1000, 1),  # Many zeros after negative
        ([-1] * 500 + [0] * 500 + [1] * 500, 500),  # Equal distribution
        ([-2, -1, 0, 0, 0, 1, 2], 2),  # Multiple zeros in middle
        ([1] * 1000, 1000),  # All same positive number
        ([-1] * 1000, 1000),  # All same negative number
    ]
    for nums, expected in test_cases:
        assert binary_search_solution.maximumCount(nums) == expected
