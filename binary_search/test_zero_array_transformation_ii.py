import pytest
from .zero_array_transformation_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_basic_functionality(solution):
    test_cases = [
        (
            [2, 3, 1],
            [[0, 2, 3]],
            1,  # Single query with sufficient value
        ),
        (
            [1, 2, 3],
            [[0, 2, 3], [0, 1, 2]],
            1,  # First query is sufficient
        ),
        (
            [1, 1, 1],
            [[0, 2, 2], [0, 1, 1]],
            1,  # First query is sufficient
        ),
    ]
    for nums, queries, expected in test_cases:
        assert solution.minZeroArray(nums, queries) == expected


def test_edge_cases(solution):
    test_cases = [
        (
            [1],
            [[0, 0, 1]],
            1,  # Single element array
        ),
        (
            [0, 0, 0],
            [[0, 2, 1]],
            0,  # Already zero array
        ),
        (
            [5],
            [[0, 0, 1]],
            -1,  # Cannot form zero array
        ),
        (
            [1, 2],
            [],
            -1,  # No queries available
        ),
    ]
    for nums, queries, expected in test_cases:
        assert solution.minZeroArray(nums, queries) == expected


def test_special_cases(solution):
    test_cases = [
        (
            [3, 3, 3],
            [[0, 2, 3], [0, 2, 3], [0, 2, 3]],
            1,  # Single query with sufficient value
        ),
        (
            [2, 2, 2],
            [[0, 2, 2], [0, 2, 1], [0, 2, 1]],
            1,  # First query is sufficient
        ),
        (
            [1, 2, 3, 4],
            [[0, 3, 4], [0, 2, 3], [1, 3, 2], [0, 1, 1]],
            1,  # First query has max value needed
        ),
    ]
    for nums, queries, expected in test_cases:
        assert solution.minZeroArray(nums, queries) == expected


def test_binary_search_specific(solution):
    """Test cases specifically designed for binary search edge cases"""
    test_cases = [
        (
            [10] * 5,
            [[0, 4, 10]] + [[0, 4, 2]] * 4,
            1,  # First query is sufficient
        ),
        (
            [1, 2, 3, 4, 5],
            [[0, 4, 5], [0, 3, 4], [0, 2, 3], [0, 1, 2], [0, 0, 1]],
            1,  # First query covers all elements
        ),
        (
            [5, 4, 3, 2, 1],
            [[0, 4, 5], [0, 3, 4], [0, 2, 3], [0, 1, 2], [0, 0, 1]],
            1,  # First query covers max value
        ),
    ]
    for nums, queries, expected in test_cases:
        assert solution.minZeroArray(nums, queries) == expected


def test_can_form_zero_array(solution):
    """Test the helper function directly"""
    test_cases = [
        (
            [1, 1, 1],
            [[0, 2, 1]],
            1,
            True,  # Single query covers all elements
        ),
        (
            [2, 2, 2],
            [[0, 1, 1], [1, 2, 1]],
            1,
            False,  # Not enough queries processed
        ),
        (
            [1, 2, 3],
            [[0, 2, 3]],
            1,
            True,  # Single query with large value
        ),
        (
            [5, 5, 5],
            [[0, 2, 1], [0, 2, 1], [0, 2, 1]],
            2,
            False,  # Need more queries
        ),
    ]
    for nums, queries, k, expected in test_cases:
        assert solution.can_form_zero_array(nums, queries, k) == expected
