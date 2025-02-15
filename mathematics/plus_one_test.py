from mathematics.plus_one import Solution
import pytest


@pytest.fixture
def solution():
    return Solution()


def test_basic_no_carry(solution):
    # Test cases where no carry is needed
    assert solution.plusOne([1, 2, 3]) == [1, 2, 4]
    assert solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert solution.plusOne([0]) == [1]


def test_single_carry(solution):
    # Test cases where single carry is needed
    assert solution.plusOne([1, 2, 9]) == [1, 3, 0]
    assert solution.plusOne([4, 3, 9, 9]) == [4, 4, 0, 0]
    assert solution.plusOne([9]) == [1, 0]


def test_multiple_carries(solution):
    # Test cases where multiple carries are needed
    assert solution.plusOne([1, 9, 9]) == [2, 0, 0]
    assert solution.plusOne([2, 9, 9, 9]) == [3, 0, 0, 0]
    assert solution.plusOne([9, 9, 9, 9]) == [1, 0, 0, 0, 0]


def test_all_nines(solution):
    # Test cases with all nines of different lengths
    assert solution.plusOne([9]) == [1, 0]
    assert solution.plusOne([9, 9]) == [1, 0, 0]
    assert solution.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert solution.plusOne([9, 9, 9, 9]) == [1, 0, 0, 0, 0]


def test_single_digit(solution):
    # Test single digit numbers
    assert solution.plusOne([0]) == [1]
    assert solution.plusOne([1]) == [2]
    assert solution.plusOne([8]) == [9]
    assert solution.plusOne([9]) == [1, 0]


def test_leading_zeros(solution):
    # Test numbers with leading zeros (although not a typical input)
    assert solution.plusOne([0, 0, 1]) == [0, 0, 2]
    assert solution.plusOne([0, 0, 9]) == [0, 1, 0]
    assert solution.plusOne([0, 9, 9]) == [1, 0, 0]


def test_large_numbers(solution):
    # Test larger numbers
    assert solution.plusOne([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 9, 0]
    assert solution.plusOne([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 2]
    assert solution.plusOne([1, 0, 0, 0, 0, 0, 0, 0, 0]) == [1, 0, 0, 0, 0, 0, 0, 0, 1]


def test_edge_cases(solution):
    # Test edge cases
    assert solution.plusOne([0]) == [1]  # Smallest possible input
    assert solution.plusOne([9, 9, 9, 9, 9, 9, 9, 9, 9]) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # All nines
    assert solution.plusOne([1, 0, 0, 0, 0]) == [1, 0, 0, 0, 1]  # Number ending with zeros


def test_consecutive_carries(solution):
    # Test numbers that require consecutive carries
    assert solution.plusOne([1, 9, 9]) == [2, 0, 0]
    assert solution.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert solution.plusOne([4, 9, 9, 9]) == [5, 0, 0, 0]


def test_alternating_digits(solution):
    # Test numbers with alternating patterns
    assert solution.plusOne([1, 0, 1, 0]) == [1, 0, 1, 1]
    assert solution.plusOne([9, 0, 9, 0]) == [9, 0, 9, 1]
    assert solution.plusOne([9, 0, 9, 9]) == [9, 1, 0, 0]
