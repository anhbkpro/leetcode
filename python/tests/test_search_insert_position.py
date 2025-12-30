from typing import List

import pytest

from binary_search.search_insert_position import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([1, 3, 5, 6], 5, 2),  # Target exists in array
        ([1, 3, 5, 6], 2, 1),  # Target should be inserted in middle
        ([1, 3, 5, 6], 7, 4),  # Target should be inserted at end
        ([1, 3, 5, 6], 0, 0),  # Target should be inserted at beginning
        ([1], 0, 0),  # Single element array, insert at beginning
        ([1], 2, 1),  # Single element array, insert at end
        ([1, 3], 2, 1),  # Two elements array, insert in middle
        ([1, 3, 5, 7, 9], 8, 4),  # Larger array, insert in middle
        ([1, 3, 5, 7, 9], 6, 3),  # Larger array, insert between elements
        ([1, 1, 1, 1], 1, 0),  # Array with duplicate elements, target exists
    ],
)
def test_search_insert(solution, nums: List[int], target: int, expected: int):
    """Test finding insert position of target in sorted array"""
    assert solution.searchInsert(nums, target) == expected
