# ruff: noqa: S101
import pytest

from sliding_windows.minimum_recolors_to_get_k_consecutive_black_blocks import Solution


@pytest.fixture
def solution():
    return Solution()


def test_basic_cases(solution):
    # Test basic cases with mix of black and white blocks
    assert (
        solution.minimumRecolors("WBBWWW", 4) == 2
    )  # Need to recolor 2 W's to get "BBBB"
    assert solution.minimumRecolors("WBWBBB", 2) == 0  # Already have "BB"


def test_all_white_blocks(solution):
    # Test cases with all white blocks
    assert solution.minimumRecolors("WWWW", 2) == 2  # Need to recolor 2 W's
    assert solution.minimumRecolors("WWW", 3) == 3  # Need to recolor all W's


def test_all_black_blocks(solution):
    # Test cases with all black blocks
    assert (
        solution.minimumRecolors("BBBB", 2) == 0
    )  # Already have consecutive black blocks
    assert (
        solution.minimumRecolors("BBB", 3) == 0
    )  # Already have consecutive black blocks


def test_invalid_length(solution):
    # Test cases where k is larger than blocks length
    assert solution.minimumRecolors("BB", 3) == -1
    assert solution.minimumRecolors("WWW", 4) == -1


def test_edge_cases(solution):
    # Test edge cases with k=1 and minimum length strings
    assert solution.minimumRecolors("W", 1) == 1
    assert solution.minimumRecolors("B", 1) == 0


@pytest.mark.parametrize(
    "blocks,k,expected",
    [
        ("WBBWWW", 4, 2),  # Need to recolor 2 W's
        ("WBWBBB", 2, 0),  # Already have BB
        ("WWWW", 2, 2),  # Need to recolor 2 W's
        ("BBBB", 2, 0),  # Already have BB
        ("BB", 3, -1),  # Invalid length
        ("W", 1, 1),  # Single white block
        ("B", 1, 0),  # Single black block
    ],
)
def test_parametrized_cases(solution, blocks, k, expected):
    assert solution.minimumRecolors(blocks, k) == expected
