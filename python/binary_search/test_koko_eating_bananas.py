import pytest

from .koko_eating_bananas import Solution


@pytest.fixture
def solution():
    return Solution()


def test_basic_functionality(solution):
    assert solution.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23


def test_edge_cases(solution):
    # Single pile
    assert solution.minEatingSpeed([1], 1) == 1
    assert solution.minEatingSpeed([10], 5) == 2

    # Hours equal to number of piles
    assert solution.minEatingSpeed([3, 6, 7, 11], 4) == 11


def test_boundary_conditions(solution):
    # Maximum possible pile
    assert solution.minEatingSpeed([1000000000], 1) == 1000000000

    # Minimum eating speed when h is maximum possible
    assert solution.minEatingSpeed([1, 1, 1, 1], 10) == 1

    # When h is exactly sum of ceil(pile/k) for some k
    assert solution.minEatingSpeed([3, 3, 3, 3], 4) == 3
