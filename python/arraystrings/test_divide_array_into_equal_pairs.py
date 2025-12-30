# ruff: noqa: S101
import pytest

from .divide_array_into_equal_pairs import Solution


@pytest.fixture
def solution():
    return Solution()


def test_valid_pairs(solution):
    # Test cases where array can be divided into equal pairs
    assert solution.divideArray(
        [1, 1, 2, 2, 3, 3]
    )  # Simple case with consecutive pairs
    assert solution.divideArray([2, 2, 2, 2])  # Multiple pairs of same number
    assert solution.divideArray([1, 2, 1, 2])  # Interleaved pairs


def test_invalid_pairs(solution):
    # Test cases where array cannot be divided into equal pairs
    assert not solution.divideArray([1, 1, 2, 3])  # Odd frequency for 2 and 3
    assert not solution.divideArray([1, 2, 3])  # Odd length array
    assert not solution.divideArray([1, 1, 1])  # Odd frequency


def test_single_number_multiple_pairs(solution):
    # Test cases with single number appearing multiple times
    assert solution.divideArray([4, 4, 4, 4, 4, 4])  # Three pairs of 4
    assert not solution.divideArray([4, 4, 4])  # Cannot form pairs with three 4s
    assert solution.divideArray([2, 2])  # Single pair


def test_mixed_numbers(solution):
    # Test cases with mix of different numbers
    assert solution.divideArray([5, 5, 8, 8, 2, 2, 3, 3])  # Multiple different pairs
    assert not solution.divideArray([5, 5, 8, 8, 2, 3])  # One unpaired number
    assert solution.divideArray([1, 1, 2, 2, 3, 3, 4, 4])  # Sequential pairs


def test_edge_cases(solution):
    # Test edge cases
    assert solution.divideArray([1, 1])  # Minimum valid case
    assert not solution.divideArray([1])  # Single element
    assert solution.divideArray([100, 100, 200, 200])  # Large numbers


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 1, 2, 2, 3, 3], True),  # Basic valid case
        ([1, 1, 2, 3], False),  # Cannot form pairs
        ([4, 4, 4, 4], True),  # Multiple pairs of same number
        ([1], False),  # Single element
        ([1, 2], False),  # Two different numbers
        ([5, 5, 8, 8, 2, 2], True),  # Multiple different pairs
    ],
)
def test_parametrized_cases(solution, nums, expected):
    assert solution.divideArray(nums) == expected
