from typing import List

import pytest

from sliding_windows.maximum_average_subarray_i import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),  # Example case
        ([5], 1, 5.0),  # Single element
        ([-1], 1, -1.0),  # Single negative element
        ([1, 2, 3, 4, 5], 1, 5.0),  # k=1, should return max element
        ([1, 2, 3, 4, 5], 5, 3.0),  # k equals array length
        ([-1, -2, -3, -4, -5], 3, -2.0),  # All negative numbers
        ([2, 2, 2, 2, 2], 3, 2.0),  # All same numbers
        ([1, 12, -5, -6, 50, 3], 1, 50.0),  # k=1 with mixed numbers
        ([-1, -2, 0, 0, -3, -4], 2, 0.0),  # Zeros in array
        ([1, 2, 3, 4, 5, 6, 7], 4, 5.5),  # Longer sequence
    ],
)
def test_find_max_average(solution, nums: List[int], k: int, expected: float):
    """Test finding the maximum average of a contiguous subarray of size k"""
    assert (
        abs(solution.findMaxAverage(nums, k) - expected) < 1e-5
    )  # Use small epsilon for float comparison
