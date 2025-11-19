from .minimum_operations_to_exceed_threshold_value_ii import Solution
import pytest


@pytest.fixture
def solution():
    return Solution()


def test_basic_case(solution):
    # Test case from LeetCode example
    nums = [2, 11, 10, 1, 3]
    k = 10
    assert solution.minOperations(nums, k) == 2


def test_no_operations_needed(solution):
    # Test when all numbers are already >= k
    nums = [10, 11, 12, 13]
    k = 10
    assert solution.minOperations(nums, k) == 0


def test_single_operation(solution):
    # Test when only one operation is needed
    nums = [4, 4]
    k = 10
    assert solution.minOperations(nums, k) == 1


def test_large_numbers(solution):
    # Test with large numbers
    nums = [1000, 2000]
    k = 4000
    assert solution.minOperations(nums, k) == 1  # 2000 + 1000*2 = 4000


def test_same_numbers(solution):
    # Test with identical numbers
    nums = [2, 2, 2, 2]
    k = 10
    assert solution.minOperations(nums, k) == 3


def test_minimum_length(solution):
    # Test with minimum length array (2 elements)
    nums = [1]
    k = 10
    assert solution.minOperations(nums, k) == 0


def test_empty_array(solution):
    # Test with empty array
    nums = []
    k = 10
    assert solution.minOperations(nums, k) == 0


def test_impossible_case(solution):
    # Test when it's impossible to reach k
    nums = [1, 1]
    k = 10
    assert solution.minOperations(nums, k) == -1


def test_exact_threshold(solution):
    # Test when result exactly equals k
    nums = [3, 3]
    k = 9
    assert solution.minOperations(nums, k) == 1  # 3*2 + 3 = 9
