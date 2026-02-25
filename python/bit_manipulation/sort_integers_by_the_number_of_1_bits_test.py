import pytest
from .sort_integers_by_the_number_of_1_bits import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case(solution):
    arr = [0,1,2,3,4,5,6,7,8]
    expected = [0,1,2,4,8,3,5,6,7]
    assert solution.sortByBits(arr) == expected


def test_same_bit_count(solution):
    arr = [3,5,6]   # all have 2 bits
    expected = [3,5,6]
    assert solution.sortByBits(arr) == expected


def test_single_element(solution):
    assert solution.sortByBits([10]) == [10]


def test_empty_array(solution):
    assert solution.sortByBits([]) == []


def test_random_case(solution):
    arr = [10,100,1000,1]
    expected = [1,10,100,1000]
    assert solution.sortByBits(arr) == expected
