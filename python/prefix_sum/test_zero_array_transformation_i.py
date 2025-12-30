import pytest

from .zero_array_transformation_i import Solution


@pytest.fixture
def solution():
    return Solution()


def test_empty_array(solution):
    nums = []
    queries = []
    assert solution.isZeroArray(nums, queries) is True


def test_single_element_zero_operations(solution):
    nums = [0]
    queries = []
    assert solution.isZeroArray(nums, queries) is True


def test_single_element_with_operation(solution):
    nums = [1]
    queries = [[0, 0]]
    assert solution.isZeroArray(nums, queries) is True


def test_single_element_insufficient_operations(solution):
    nums = [2]
    queries = [[0, 0]]
    assert solution.isZeroArray(nums, queries) is False


def test_multiple_elements_all_zeros(solution):
    nums = [0, 0, 0]
    queries = []
    assert solution.isZeroArray(nums, queries) is True


def test_multiple_elements_sufficient_operations(solution):
    nums = [1, 2, 1]
    queries = [[0, 1], [1, 2]]
    assert solution.isZeroArray(nums, queries) is True


def test_multiple_elements_insufficient_operations(solution):
    nums = [2, 3, 1]
    queries = [[0, 1], [1, 2]]
    assert solution.isZeroArray(nums, queries) is False


def test_overlapping_queries(solution):
    nums = [2, 2, 2]
    queries = [[0, 1], [1, 2], [0, 2]]
    assert solution.isZeroArray(nums, queries) is True


def test_unsorted_queries(solution):
    nums = [1, 2, 1]
    queries = [[1, 2], [0, 1]]
    assert solution.isZeroArray(nums, queries) is True


def test_leetcode_example_1(solution):
    nums = [1, 2, 3]
    queries = [[1, 2], [0, 1], [0, 2]]
    assert solution.isZeroArray(nums, queries) is False


def test_leetcode_example_2(solution):
    nums = [1, 2, 3]
    queries = [[1, 2], [0, 1]]
    assert solution.isZeroArray(nums, queries) is False


def test_large_numbers(solution):
    nums = [100, 200, 300]
    queries = [[0, 0], [1, 1], [2, 2], [0, 2]]
    assert solution.isZeroArray(nums, queries) is False


def test_single_operation_covering_all(solution):
    nums = [1, 1, 1]
    queries = [[0, 2]]
    assert solution.isZeroArray(nums, queries) is True


def test_multiple_operations_same_range(solution):
    nums = [3, 3, 3]
    queries = [[0, 2], [0, 2], [0, 2]]
    assert solution.isZeroArray(nums, queries) is True
