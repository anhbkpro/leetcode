import pytest

from .alternating_groups_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_basic_alternating_sequence(solution):
    assert solution.numberOfAlternatingGroups([1, 0, 1, 0, 1], 3) == 3


def test_no_alternating_sequence(solution):
    assert solution.numberOfAlternatingGroups([1, 1, 1, 0, 0], 3) == 0


def test_minimum_length_array(solution):
    assert solution.numberOfAlternatingGroups([1, 0, 1], 3) == 1


def test_k_equals_length(solution):
    assert solution.numberOfAlternatingGroups([1, 0, 1, 0, 1], 5) == 1


def test_circular_sequence(solution):
    assert solution.numberOfAlternatingGroups([1, 0, 1, 0, 1], 3) == 3
    assert solution.numberOfAlternatingGroups([0, 1, 0, 1, 0], 3) == 3


def test_multiple_values_binary(solution):
    assert solution.numberOfAlternatingGroups([1, 0, 1, 0, 1, 0], 4) == 6


def test_longer_sequence(solution):
    # Test with a longer sequence to ensure it handles larger inputs
    colors = [1, 0] * 50  # length 100
    assert solution.numberOfAlternatingGroups(colors, 3) > 0


def test_edge_cases_within_constraints(solution):
    # k equals array length
    assert solution.numberOfAlternatingGroups([1, 0, 1], 3) == 1
    # Minimum array length with minimum k
    assert solution.numberOfAlternatingGroups([1, 0, 1], 3) == 1
    # All zeros then all ones
    assert solution.numberOfAlternatingGroups([0, 0, 0, 1, 1], 3) == 0
