# ruff: noqa: S101
import pytest
from .trapping_rain_water import BruteForce, DynamicProgramming, Stack, TwoPointers


@pytest.fixture
def solutions():
    return [BruteForce(), DynamicProgramming(), Stack(), TwoPointers()]


def test_basic_cases(solutions):
    # Test basic cases with clear trapping areas
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected = 6  # Water trapped: 1 + 1 + 2 + 1 + 1 = 6
    for solution in solutions:
        assert solution.trap(height) == expected


def test_no_trap(solutions):
    # Test cases where no water can be trapped
    test_cases = [
        [1, 2, 3, 4, 5],  # Increasing heights
        [5, 4, 3, 2, 1],  # Decreasing heights
        [1, 1, 1, 1],  # Equal heights
    ]
    for height in test_cases:
        for solution in solutions:
            assert solution.trap(height) == 0


def test_symmetric_cases(solutions):
    # Test symmetric height patterns
    test_cases = [
        ([2, 0, 2], 2),  # Simple valley
        ([3, 0, 0, 3], 6),  # Wide valley
        ([4, 2, 0, 2, 4], 8),  # Valley with steps
    ]
    for height, expected in test_cases:
        for solution in solutions:
            assert solution.trap(height) == expected


def test_edge_cases(solutions):
    # Test edge cases
    test_cases = [
        ([], 0),  # Empty array
        ([5], 0),  # Single element
        ([5, 5], 0),  # Two elements
        ([0, 0, 0], 0),  # All zeros
    ]
    for height, expected in test_cases:
        for solution in solutions:
            assert solution.trap(height) == expected


def test_complex_cases(solutions):
    # Test more complex patterns
    test_cases = [
        ([5, 2, 1, 2, 1, 5], 14),  # Deep valley with uneven bottom
        ([1, 4, 2, 5, 1, 2, 3], 5),  # Multiple peaks and valleys
        ([4, 2, 3, 1, 2], 2),  # Multiple local maxima
    ]
    for height, expected in test_cases:
        for solution in solutions:
            assert solution.trap(height) == expected


@pytest.mark.parametrize(
    "height,expected",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),  # Standard case
        ([2, 0, 2], 2),  # Simple valley
        ([3, 0, 0, 3], 6),  # Wide valley
        ([], 0),  # Empty array
        ([5], 0),  # Single element
        ([1, 2, 3, 4, 5], 0),  # No trap possible
        ([5, 2, 1, 2, 1, 5], 14),  # Deep valley
    ],
)
def test_parametrized_cases(solutions, height, expected):
    for solution in solutions:
        assert solution.trap(height) == expected
