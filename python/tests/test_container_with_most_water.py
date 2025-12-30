from typing import List

import pytest

from two_pointers.container_with_most_water import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "height,expected",
    [
        (
            [1, 8, 6, 2, 5, 4, 8, 3, 7],
            49,
        ),  # Example case with max area between heights 8 and 7
        ([1, 1], 1),  # Minimum case with two lines
        ([4, 3, 2, 1, 4], 16),  # Max area using first and last lines
        ([1, 2, 4, 3], 4),  # Max area between middle elements
        ([1, 2, 1], 2),  # Small array with different heights
        ([1, 1, 1, 1], 3),  # Equal heights
        (
            [1, 8, 6, 2, 5, 4, 8, 3, 7, 9],
            64,
        ),  # Larger array with max area between two 8s
        ([2, 3, 4, 5, 18, 17, 6], 17),  # Max area between highest elements
        ([1], 0),  # Single element (no container possible)
        ([], 0),  # Empty array
        ([5, 5, 5, 5, 5], 20),  # All equal heights
        ([1, 2, 3, 4, 5], 6),  # Ascending heights
        ([5, 4, 3, 2, 1], 6),  # Descending heights
        ([1, 3, 2, 5, 25, 24, 5], 24),  # Complex case with multiple peaks
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25),  # Large ascending array
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 25),  # Large descending array
        ([1, 8, 6, 2, 5, 4, 8, 25, 7], 49),  # Modified classic case
        ([2, 1], 1),  # Two elements with different heights
        ([3, 9, 3, 4, 7, 2, 12, 6], 45),  # Another complex case
    ],
)
def test_max_area(solution, height: List[int], expected: int):
    """Test finding the maximum area that can be contained"""
    assert solution.maxArea(height) == expected


def test_max_area_edge_cases(solution):
    """Test edge cases for max area calculation"""
    # Test with very large numbers
    assert solution.maxArea([1000000, 1, 1000000]) == 2000000

    # Test with zero heights
    assert solution.maxArea([0, 1, 0]) == 0

    # Test with negative heights (should handle gracefully)
    assert solution.maxArea([-1, 1, -1]) == 0


def test_max_area_performance_cases(solution):
    """Test performance edge cases"""
    # Large array with all same values
    large_array = [5] * 1000
    expected = 5 * 999  # height * width
    assert solution.maxArea(large_array) == expected

    # Array with alternating high and low values
    alternating = [10, 1, 10, 1, 10, 1, 10]
    assert solution.maxArea(alternating) == 60  # 10 * 6


def test_max_area_return_type(solution):
    """Test that the function returns the correct type"""
    result = solution.maxArea([1, 2, 3])
    assert isinstance(result, int)
    assert result >= 0


def test_max_area_immutable_input(solution):
    """Test that the input array is not modified"""
    original = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    original_copy = original.copy()
    solution.maxArea(original)
    assert original == original_copy
