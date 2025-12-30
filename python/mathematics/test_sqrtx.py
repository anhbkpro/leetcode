import pytest

from mathematics.sqrtx import SolutionBinarySearch


@pytest.fixture
def solution():
    return SolutionBinarySearch()


def test_perfect_squares(solution):
    # Test perfect square numbers
    assert solution.mySqrt(0) == 0
    assert solution.mySqrt(1) == 1
    assert solution.mySqrt(4) == 2
    assert solution.mySqrt(9) == 3
    assert solution.mySqrt(16) == 4
    assert solution.mySqrt(25) == 5
    assert solution.mySqrt(36) == 6
    assert solution.mySqrt(49) == 7
    assert solution.mySqrt(64) == 8
    assert solution.mySqrt(81) == 9
    assert solution.mySqrt(100) == 10


def test_non_perfect_squares(solution):
    # Test non-perfect square numbers
    assert solution.mySqrt(2) == 1
    assert solution.mySqrt(3) == 1
    assert solution.mySqrt(5) == 2
    assert solution.mySqrt(8) == 2
    assert solution.mySqrt(10) == 3
    assert solution.mySqrt(15) == 3
    assert solution.mySqrt(24) == 4
    assert solution.mySqrt(99) == 9


def test_edge_cases(solution):
    # Test edge cases
    assert solution.mySqrt(0) == 0  # Smallest valid input
    assert solution.mySqrt(1) == 1  # Smallest perfect square
    assert solution.mySqrt(2) == 1  # Smallest non-perfect square


def test_large_numbers(solution):
    # Test large numbers
    assert solution.mySqrt(1000000) == 1000
    assert solution.mySqrt(2147483647) == 46340  # Maximum 32-bit integer
    assert solution.mySqrt(999999999) == 31622


def test_consecutive_numbers(solution):
    # Test consecutive numbers to ensure proper rounding
    assert solution.mySqrt(10) == 3
    assert solution.mySqrt(11) == 3
    assert solution.mySqrt(12) == 3
    assert solution.mySqrt(13) == 3
    assert solution.mySqrt(14) == 3
    assert solution.mySqrt(15) == 3
    assert solution.mySqrt(16) == 4  # Perfect square
    assert solution.mySqrt(17) == 4


def test_binary_search_boundaries(solution):
    # Test numbers near perfect squares
    assert solution.mySqrt(15) == 3  # Just before 16
    assert solution.mySqrt(16) == 4  # Perfect square
    assert solution.mySqrt(17) == 4  # Just after 16
    assert solution.mySqrt(24) == 4  # Just before 25
    assert solution.mySqrt(25) == 5  # Perfect square
    assert solution.mySqrt(26) == 5  # Just after 25


def test_power_of_two(solution):
    # Test powers of 2
    assert solution.mySqrt(1) == 1  # 2^0
    assert solution.mySqrt(2) == 1
    assert solution.mySqrt(4) == 2  # 2^2
    assert solution.mySqrt(8) == 2
    assert solution.mySqrt(16) == 4  # 2^4
    assert solution.mySqrt(32) == 5
    assert solution.mySqrt(64) == 8  # 2^6
    assert solution.mySqrt(128) == 11


def test_near_perfect_squares(solution):
    # Test numbers near perfect squares
    assert solution.mySqrt(99) == 9  # Just before 100
    assert solution.mySqrt(100) == 10  # Perfect square
    assert solution.mySqrt(101) == 10  # Just after 100
    assert solution.mySqrt(120) == 10  # Between 100 and 121
    assert solution.mySqrt(121) == 11  # Perfect square
    assert solution.mySqrt(122) == 11  # Just after 121
