import pytest

from hashing.find_missing_and_repeated_values import Solution


@pytest.fixture
def solution():
    return Solution()


def test_2x2_grid(solution):
    # Test case for 2x2 grid
    grid = [[1, 2], [2, 3]]  # 2 is repeated, 4 is missing
    assert solution.findMissingAndRepeatedValues(grid) == [2, 4]  # noqa: S101


def test_3x3_grid(solution):
    # Test case for 3x3 grid
    grid = [[1, 2, 3], [2, 4, 5], [6, 7, 8]]  # 2 is repeated, 9 is missing
    assert solution.findMissingAndRepeatedValues(grid) == [2, 9]  # noqa: S101


def test_4x4_grid(solution):
    # Test case for 4x4 grid
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 14, 16],  # 14 is repeated, 15 is missing
    ]
    assert solution.findMissingAndRepeatedValues(grid) == [14, 15]  # noqa: S101


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([[1, 2], [2, 3]], [2, 4]),  # 2x2: 2 repeated, 4 missing
        ([[1, 2, 3], [2, 4, 5], [6, 7, 8]], [2, 9]),  # 3x3: 2 repeated, 9 missing
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 14, 16]],
            [14, 15],
        ),  # 4x4: 14 repeated, 15 missing
    ],
)
def test_parametrized_cases(solution, grid, expected):
    assert solution.findMissingAndRepeatedValues(grid) == expected  # noqa: S101
