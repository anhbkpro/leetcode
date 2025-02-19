import pytest
from typing import List
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
    ],
)
def test_max_area(solution, height: List[int], expected: int):
    """Test finding the maximum area that can be contained"""
    assert solution.maxArea(height) == expected
