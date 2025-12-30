from typing import List

import pytest

from backtracking.find_unique_binary_string import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums,expected_length",
    [
        (["01", "10"], 2),  # Basic case, "00" or "11" would be valid
        (["0"], 1),  # Single element case
        (["00", "01"], 2),  # Sequential patterns
        (["0000", "0001", "0010", "0011"], 4),  # Longer strings
    ],
)
def test_find_different_binary_string(solution, nums: List[str], expected_length: int):
    """Test finding a binary string that's different from all strings in nums"""
    result = solution.findDifferentBinaryString(nums)

    # Check that result has correct length
    assert len(result) == expected_length

    # Check that result is a valid binary string
    assert all(c in "01" for c in result)

    # Check that result is not in nums
    assert result not in nums

    # Check that result is a valid binary string of the correct length
    assert len(result) == len(nums[0])
