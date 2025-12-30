import pytest

from arraystrings.count_total_number_of_colored_cells import Solution


@pytest.fixture
def solution():
    return Solution()


def test_base_cases(solution):
    # Test cases for n = 1
    assert solution.coloredCells(1) == 1  # noqa: S101


def test_small_numbers(solution):
    # Test cases for n = 2, 3
    assert solution.coloredCells(2) == 5  # noqa: S101  # 1 + 4
    assert solution.coloredCells(3) == 13  # noqa: S101  # 1 + 4 + 8


def test_medium_numbers(solution):
    # Test cases for n = 4, 5
    assert solution.coloredCells(4) == 25  # noqa: S101  # 1 + 4 + 8 + 12
    assert solution.coloredCells(5) == 41  # noqa: S101  # 1 + 4 + 8 + 12 + 16


@pytest.mark.parametrize(
    "input_num,expected",
    [
        (1, 1),  # Base case
        (2, 5),  # 1 + 4
        (3, 13),  # 1 + 4 + 8
        (4, 25),  # 1 + 4 + 8 + 12
        (5, 41),  # 1 + 4 + 8 + 12 + 16
    ],
)
def test_parametrized_cases(solution, input_num, expected):
    assert solution.coloredCells(input_num) == expected  # noqa: S101
