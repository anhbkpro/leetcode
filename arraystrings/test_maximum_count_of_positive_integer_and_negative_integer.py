import pytest
from .maximum_count_of_positive_integer_and_negative_integer import (
    Solution,
    BinarySearchSolution,
)


@pytest.fixture
def solution():
    return Solution()


@pytest.fixture
def binary_search_solution():
    return BinarySearchSolution()


def test_basic_functionality(solution):
    assert solution.maximumCount([-2, -1, -1, 1, 2, 3]) == 3
    assert solution.maximumCount([-3, -2, -1, 0, 0, 1, 2]) == 3
    assert solution.maximumCount([1, 2, 3, 4, 5]) == 5


def test_edge_cases(solution):
    # Empty array
    assert solution.maximumCount([]) == 0
    # Array with only zeros
    assert solution.maximumCount([0, 0, 0]) == 0
    # Single element arrays
    assert solution.maximumCount([1]) == 1
    assert solution.maximumCount([-1]) == 1
    assert solution.maximumCount([0]) == 0


def test_special_cases(solution):
    # All negative numbers
    assert solution.maximumCount([-3, -2, -1]) == 3
    # All positive numbers
    assert solution.maximumCount([1, 2, 3]) == 3
    # More zeros than positives or negatives
    assert solution.maximumCount([-1, 0, 0, 0, 0, 1]) == 1
    # Equal number of positives and negatives
    assert solution.maximumCount([-2, -1, 1, 2]) == 2


def test_input_variations(solution):
    # Large numbers
    assert solution.maximumCount([-1000000, 1000000]) == 1
    # Consecutive numbers
    assert solution.maximumCount([-2, -1, 0, 1, 2]) == 2
    # Duplicate numbers
    assert solution.maximumCount([-2, -2, 1, 1, 1]) == 3
    # Mixed order
    assert solution.maximumCount([2, -1, 0, 1, -2]) == 2
