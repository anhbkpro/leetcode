import pytest
from typing import List
from two_pointers.move_zeroes import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1], [1]),
        ([0, 0, 0, 1], [1, 0, 0, 0]),
        ([1, 2, 3, 0, 0], [1, 2, 3, 0, 0]),
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        ([1, 0, 1], [1, 1, 0]),
    ],
)
def test_move_zeroes(solution, nums: List[int], expected: List[int]):
    """Test moving zeroes to the end while maintaining relative order of non-zero elements"""
    solution.moveZeroes(nums)
    assert nums == expected
