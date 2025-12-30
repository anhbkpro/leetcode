import pytest

from .find_the_maximum_sum_of_node_values import Solution


@pytest.fixture
def solution():
    return Solution()


def test_empty_array(solution):
    nums = []
    k = 2
    edges = []
    assert solution.maximumValueSum(nums, k, edges) == 0


def test_single_node(solution):
    nums = [1]
    k = 2
    edges = []
    assert solution.maximumValueSum(nums, k, edges) == 1


def test_two_nodes_no_xor_needed(solution):
    nums = [1, 2]
    k = 2
    edges = [[0, 1]]
    assert solution.maximumValueSum(nums, k, edges) == 3


def test_two_nodes_xor_beneficial(solution):
    nums = [1, 2]
    k = 3
    edges = [[0, 1]]
    assert solution.maximumValueSum(nums, k, edges) == 3


def test_leetcode_example_1(solution):
    nums = [1, 2, 1]
    k = 3
    edges = [[0, 1], [0, 2]]
    assert (
        solution.maximumValueSum(nums, k, edges) == 6
    )  # (1^3) + 2 + (1^3) = 2 + 2 + 2 = 6


def test_leetcode_example_2(solution):
    nums = [2, 3]
    k = 7
    edges = [[0, 1]]
    assert solution.maximumValueSum(nums, k, edges) == 9  # (2^7) + (3^7) = 5 + 4 = 9


def test_three_nodes_linear(solution):
    nums = [1, 2, 3]
    k = 2
    edges = [[0, 1], [1, 2]]
    assert solution.maximumValueSum(nums, k, edges) == 6


def test_three_nodes_star(solution):
    nums = [1, 2, 3]
    k = 2
    edges = [[0, 1], [0, 2]]
    assert solution.maximumValueSum(nums, k, edges) == 6


def test_four_nodes_square(solution):
    nums = [1, 2, 3, 4]
    k = 2
    edges = [[0, 1], [1, 2], [2, 3], [3, 0]]
    assert solution.maximumValueSum(nums, k, edges) == 14


def test_large_k_value(solution):
    nums = [1, 2, 3, 4]
    k = 10
    edges = [[0, 1], [1, 2], [2, 3]]
    assert solution.maximumValueSum(nums, k, edges) == 42


def test_negative_numbers(solution):
    nums = [-1, -2, -3]
    k = 2
    edges = [[0, 1], [1, 2]]
    assert solution.maximumValueSum(nums, k, edges) == -6


def test_zero_k_value(solution):
    nums = [1, 2, 3]
    k = 0
    edges = [[0, 1], [1, 2]]
    assert solution.maximumValueSum(nums, k, edges) == 6  # No XOR operations as k=0


def test_complex_tree(solution):
    nums = [1, 2, 3, 4, 5]
    k = 3
    edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
    assert solution.maximumValueSum(nums, k, edges) == 19
