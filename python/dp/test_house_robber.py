import pytest

from .house_robber import (
    DynamicProgramming,
    OptimizedDynamicProgramming,
    RecursionWithMemoization,
)


@pytest.fixture
def recursion_solution():
    return RecursionWithMemoization()


@pytest.fixture
def dp_solution():
    return DynamicProgramming()


@pytest.fixture
def optimized_dp_solution():
    return OptimizedDynamicProgramming()


def test_basic_functionality(recursion_solution, dp_solution, optimized_dp_solution):
    # Test case 1: Simple array with obvious optimal solution
    nums1 = [1, 2, 3, 1]  # Should rob house 1 and 3 (1 + 3 = 4)
    assert recursion_solution.rob(nums1) == 4
    assert dp_solution.rob(nums1) == 4
    assert optimized_dp_solution.rob(nums1) == 4

    # Test case 2: Alternating values
    nums2 = [2, 7, 9, 3, 1]  # Should rob house 1, 3, 5 (2 + 9 + 1 = 12)
    assert recursion_solution.rob(nums2) == 12
    assert dp_solution.rob(nums2) == 12
    assert optimized_dp_solution.rob(nums2) == 12


def test_edge_cases(recursion_solution, dp_solution, optimized_dp_solution):
    # Empty array
    assert recursion_solution.rob([]) == 0
    assert dp_solution.rob([]) == 0
    assert optimized_dp_solution.rob([]) == 0

    # Single house
    assert recursion_solution.rob([5]) == 5
    assert dp_solution.rob([5]) == 5
    assert optimized_dp_solution.rob([5]) == 5

    # Two houses
    assert recursion_solution.rob([2, 3]) == 3
    assert dp_solution.rob([2, 3]) == 3
    assert optimized_dp_solution.rob([2, 3]) == 3


def test_special_cases(recursion_solution, dp_solution, optimized_dp_solution):
    # All same values
    nums1 = [5, 5, 5, 5]  # Should rob houses 1 and 3 or 2 and 4 (5 + 5 = 10)
    assert recursion_solution.rob(nums1) == 10
    assert dp_solution.rob(nums1) == 10
    assert optimized_dp_solution.rob(nums1) == 10

    # Increasing sequence
    nums2 = [1, 2, 3, 4, 5]  # Should rob houses 1, 3, and 5 (1 + 3 + 5 = 9)
    assert recursion_solution.rob(nums2) == 9
    assert dp_solution.rob(nums2) == 9
    assert optimized_dp_solution.rob(nums2) == 9

    # Decreasing sequence
    nums3 = [5, 4, 3, 2, 1]  # Should rob houses 1, 3, and 5
    assert recursion_solution.rob(nums3) == 9
    assert dp_solution.rob(nums3) == 9
    assert optimized_dp_solution.rob(nums3) == 9


def test_large_numbers(recursion_solution, dp_solution, optimized_dp_solution):
    # Test with large numbers
    nums = [1000000, 1000000, 1000000]
    assert recursion_solution.rob(nums) == 2000000
    assert dp_solution.rob(nums) == 2000000
    assert optimized_dp_solution.rob(nums) == 2000000
