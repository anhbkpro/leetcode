import pytest
from .house_robber_iv import Solution


@pytest.fixture
def solution():
    return Solution()


def test_basic_functionality(solution):
    # Test case 1: Simple array
    nums1, k1 = [2, 3, 5, 9], 2  # Rob houses with values [2, 5] with capability 5
    assert solution.minCapability(nums1, k1) == 5

    # Test case 2: Another case
    nums2, k2 = [2, 7, 9, 3, 1], 2  # Rob houses with values [2, 1] with capability 2
    assert solution.minCapability(nums2, k2) == 2


def test_edge_cases(solution):
    # Single house
    assert solution.minCapability([5], 1) == 5

    # Two houses, rob one
    assert solution.minCapability([2, 3], 1) == 2

    # Three houses, rob two non-adjacent
    assert solution.minCapability([2, 3, 4], 2) == 4


def test_special_cases(solution):
    # All same values
    nums1, k1 = [5, 5, 5, 5], 2  # Rob any two non-adjacent houses
    assert solution.minCapability(nums1, k1) == 5

    # Increasing sequence
    nums2, k2 = [1, 2, 3, 4, 5], 3  # Rob houses with values [1, 3, 5]
    assert solution.minCapability(nums2, k2) == 5

    # Decreasing sequence
    nums3, k3 = [5, 4, 3, 2, 1], 2  # Rob houses with values [3, 1]
    assert solution.minCapability(nums3, k3) == 3


def test_boundary_conditions(solution):
    # Test with maximum possible values
    nums1 = [10**9, 10**9 - 1, 10**9 - 2]
    assert solution.minCapability(nums1, 2) == 10**9

    # Test when k is maximum possible (half of array length)
    nums2 = [1, 2, 3, 4, 5, 6]
    assert solution.minCapability(nums2, 3) == 5

    # Test when all values are minimum (1)
    nums3 = [1, 1, 1, 1]
    assert solution.minCapability(nums3, 2) == 1


def test_helper_is_valid(solution):
    # Test the _is_valid helper function
    nums = [2, 3, 5, 9]

    # Should be able to rob 2 houses with capability 5
    assert solution._is_valid(nums, 2, 5) is True

    # Should not be able to rob 2 houses with capability 2
    assert solution._is_valid(nums, 2, 2) is False

    # Should be able to rob 1 house with capability 2
    assert solution._is_valid(nums, 1, 2) is True
