import pytest
from prefix_sum.LC75__find_the_highest_altitude import Solution


def test_largest_altitude_typical():
    solution = Solution()
    gain = [-5, 1, 5, 0, -7]
    assert solution.largestAltitude(gain) == 1


def test_largest_altitude_all_positive():
    solution = Solution()
    gain = [1, 2, 3, 4, 5]
    assert solution.largestAltitude(gain) == 15


def test_largest_altitude_all_negative():
    solution = Solution()
    gain = [-1, -2, -3, -4, -5]
    assert solution.largestAltitude(gain) == 0


def test_largest_altitude_single_element():
    solution = Solution()
    assert solution.largestAltitude([5]) == 5
    assert solution.largestAltitude([-5]) == 0


def test_largest_altitude_empty():
    solution = Solution()
    assert solution.largestAltitude([]) == 0


def test_largest_altitude_alternating():
    solution = Solution()
    gain = [1, -1, 1, -1, 1]
    assert solution.largestAltitude(gain) == 1


def test_largest_altitude_plateau():
    solution = Solution()
    gain = [2, 2, 2, 2, 2]
    assert solution.largestAltitude(gain) == 10
