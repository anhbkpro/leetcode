import pytest
from .sort_colors import Solution


@pytest.fixture
def solution():
    return Solution()


def test_empty_array(solution):
    nums = []
    solution.sortColors(nums)
    assert nums == []


def test_single_element(solution):
    nums = [1]
    solution.sortColors(nums)
    assert nums == [1]


def test_all_zeros(solution):
    nums = [0, 0, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 0]


def test_all_ones(solution):
    nums = [1, 1, 1]
    solution.sortColors(nums)
    assert nums == [1, 1, 1]


def test_all_twos(solution):
    nums = [2, 2, 2]
    solution.sortColors(nums)
    assert nums == [2, 2, 2]


def test_mixed_numbers(solution):
    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_already_sorted(solution):
    nums = [0, 0, 1, 1, 2, 2]
    solution.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_reverse_sorted(solution):
    nums = [2, 2, 1, 1, 0, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_random_order(solution):
    nums = [1, 2, 0, 1, 2, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_leetcode_example(solution):
    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]
