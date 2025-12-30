# ruff: noqa: S101
import pytest

from .minimum_time_to_repair_cars import Solution


@pytest.fixture
def solution():
    return Solution()


def test_single_mechanic(solution):
    # Test cases with a single mechanic
    assert (
        solution.repairCars([4], 4) == 64
    )  # One mechanic, rank 4, repairs 4 cars: 4 * 4^2 = 64
    assert (
        solution.repairCars([5], 1) == 5
    )  # One mechanic, rank 5, repairs 1 car: 5 * 1^2 = 5
    assert (
        solution.repairCars([3], 2) == 12
    )  # One mechanic, rank 3, repairs 2 cars: 3 * 2^2 = 12


def test_multiple_mechanics_same_rank(solution):
    # Test cases with multiple mechanics of the same rank
    assert (
        solution.repairCars([4, 4], 4) == 16
    )  # Two mechanics, rank 4, each repairs 2 cars: 4 * 2^2 = 16 each
    assert (
        solution.repairCars([3, 3, 3], 3) == 3
    )  # Three mechanics, rank 3, each repairs 1 car: 3 * 1^2 = 3 each
    assert (
        solution.repairCars([2, 2], 6) == 18
    )  # Two mechanics, rank 2, each repairs 3 cars: 2 * 3^2 = 18 each


def test_multiple_mechanics_different_ranks(solution):
    # Test cases with mechanics of different ranks
    assert (
        solution.repairCars([4, 2, 3, 1], 10) == 16
    )  # Different ranks handling multiple cars
    assert (
        solution.repairCars([5, 1, 8], 6) == 16
    )  # Different ranks with uneven distribution
    assert solution.repairCars([1, 2], 8) == 25  # Two different ranks handling cars


def test_edge_cases(solution):
    # Test edge cases
    assert solution.repairCars([1], 1) == 1  # Minimum possible case
    assert solution.repairCars([100], 1) == 100  # High rank mechanic
    assert solution.repairCars([1, 1, 1], 10) == 16  # Multiple mechanics, minimum rank


def test_large_numbers(solution):
    # Test cases with larger numbers
    assert solution.repairCars([1], 100) == 10000  # Single mechanic with many cars
    assert (
        solution.repairCars([1, 1, 1, 1], 100) == 625
    )  # Multiple mechanics with many cars
    assert solution.repairCars([10, 10], 10) == 250  # Higher ranks with multiple cars


@pytest.mark.parametrize(
    "ranks,cars,expected",
    [
        ([4], 4, 64),  # Single mechanic
        ([4, 4], 4, 16),  # Multiple mechanics, same rank
        ([4, 2, 3, 1], 10, 16),  # Different ranks
        ([1], 1, 1),  # Minimum case
        ([1, 1, 1], 10, 16),  # Multiple mechanics, minimum rank
        ([5, 1, 8], 6, 16),  # Different ranks, uneven distribution
    ],
)
def test_parametrized_cases(solution, ranks, cars, expected):
    assert solution.repairCars(ranks, cars) == expected
