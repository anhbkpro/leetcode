import pytest
from .LC75__longest_subarray_of_1s_after_deleting_one_element import Solution


@pytest.fixture
def solution():
    return Solution()


def test_empty_array(solution):
    nums = []
    assert solution.longestSubarray(nums) == 0


def test_single_one(solution):
    nums = [1]
    assert solution.longestSubarray(nums) == 0  # Must delete one element


def test_single_zero(solution):
    nums = [0]
    assert solution.longestSubarray(nums) == 0  # Must delete one element


def test_all_ones(solution):
    nums = [1, 1, 1]
    assert solution.longestSubarray(nums) == 2  # Delete one 1, get 2 consecutive 1s


def test_all_zeros(solution):
    nums = [0, 0, 0]
    assert solution.longestSubarray(nums) == 0  # No 1s after deletion


def test_leetcode_example_1(solution):
    nums = [1, 1, 0, 1]
    assert solution.longestSubarray(nums) == 3  # Delete 0, get 3 consecutive 1s


def test_leetcode_example_2(solution):
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    assert solution.longestSubarray(nums) == 5  # Delete one 0, get 5 consecutive 1s


def test_alternating_ones_zeros(solution):
    nums = [1, 0, 1, 0, 1]
    assert solution.longestSubarray(nums) == 2  # Can get 2 consecutive 1s


def test_multiple_zeros(solution):
    nums = [1, 1, 0, 0, 1, 1]
    assert solution.longestSubarray(nums) == 2  # Can get 2 consecutive 1s


def test_ones_at_ends(solution):
    nums = [1, 0, 0, 0, 1]
    assert solution.longestSubarray(nums) == 1  # Can get 1 consecutive 1


def test_long_sequence(solution):
    nums = [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
    assert solution.longestSubarray(nums) == 7  # Can get 8 consecutive 1s
