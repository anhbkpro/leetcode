import pytest

from arraystrings.add_digits import Solution


@pytest.fixture
def solution():
    return Solution()


def test_single_digit_numbers(solution):
    # Test cases for numbers less than 10
    assert solution.addDigits(0) == 0  # noqa: S101
    assert solution.addDigits(1) == 1  # noqa: S101
    assert solution.addDigits(9) == 9  # noqa: S101


def test_two_digit_numbers(solution):
    # Test cases for two-digit numbers
    assert solution.addDigits(10) == 1  # noqa: S101  # 1 + 0 = 1
    assert solution.addDigits(11) == 2  # noqa: S101  # 1 + 1 = 2
    assert solution.addDigits(19) == 1  # noqa: S101  # 1 + 9 = 10 -> 1 + 0 = 1
    assert solution.addDigits(38) == 2  # noqa: S101  # 3 + 8 = 11 -> 1 + 1 = 2


def test_three_digit_numbers(solution):
    # Test cases for three-digit numbers
    assert solution.addDigits(100) == 1  # noqa: S101  # 1 + 0 + 0 = 1
    assert solution.addDigits(123) == 6  # noqa: S101  # 1 + 2 + 3 = 6
    assert solution.addDigits(999) == 9  # noqa: S101  # 9 + 9 + 9 = 27 -> 2 + 7 = 9


def test_large_numbers(solution):
    # Test cases for larger numbers
    assert (
        solution.addDigits(1234) == 1
    )  # noqa: S101  # 1 + 2 + 3 + 4 = 10 -> 1 + 0 = 1
    assert (
        solution.addDigits(9999) == 9
    )  # noqa: S101  # 9 + 9 + 9 + 9 = 36 -> 3 + 6 = 9
    assert (
        solution.addDigits(12345) == 6
    )  # noqa: S101  # 1 + 2 + 3 + 4 + 5 = 15 -> 1 + 5 = 6


@pytest.mark.parametrize(
    "input_num,expected",
    [
        (0, 0),  # Single digit
        (9, 9),  # Single digit
        (10, 1),  # Two digits
        (38, 2),  # Two digits
        (123, 6),  # Three digits
        (999, 9),  # Three digits
        (1234, 1),  # Four digits
        (9999, 9),  # Four digits
        (12345, 6),  # Five digits
    ],
)
def test_parametrized_cases(solution, input_num, expected):
    assert solution.addDigits(input_num) == expected  # noqa: S101
