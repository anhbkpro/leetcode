import pytest
from typing import List
from two_pointers.max_number_of_k_sum_pairs import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 2, 3, 4], 5, 2),  # Can form two pairs: (1,4) and (2,3)
        ([3, 1, 3, 4, 3], 6, 1),  # Can form one pair: (3,3)
        ([1, 2, 3, 4], 2, 0),  # No pairs sum to 2
        ([3, 1, 3, 4, 3], 12, 0),  # No pairs sum to 12
        ([], 1, 0),  # Empty array
        ([1], 2, 0),  # Single element
        ([1, 1, 1, 1], 2, 2),  # Multiple identical pairs
        ([2, 2, 2, 3, 1, 1, 3], 4, 3),  # Multiple valid pairs with different numbers
    ],
)
def test_max_operations(solution, nums: List[int], k: int, expected: int):
    """Test finding maximum number of operations where two numbers sum to k"""
    assert solution.maxOperations(nums, k) == expected
