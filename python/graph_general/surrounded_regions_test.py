import pytest

from .surrounded_regions import Solution


@pytest.fixture
def solution():
    return Solution()


def test_basic_surrounded_region(solution):
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    expected = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]
    solution.solve(board)
    assert board == expected


def test_border_connected_region(solution):
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "O", "O", "X"],
        ["X", "O", "X", "O"],
    ]
    expected = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "O", "O", "X"],
        ["X", "O", "X", "O"],
    ]
    solution.solve(board)
    assert board == expected


def test_empty_board(solution):
    board = []
    solution.solve(board)
    assert board == []


def test_single_row(solution):
    board = [["X", "O", "X"]]
    expected = [["X", "O", "X"]]
    solution.solve(board)
    assert board == expected


def test_single_column(solution):
    board = [["X"], ["O"], ["X"]]
    expected = [["X"], ["O"], ["X"]]
    solution.solve(board)
    assert board == expected


def test_no_o_cells(solution):
    board = [
        ["X", "X", "X"],
        ["X", "X", "X"],
        ["X", "X", "X"],
    ]
    expected = [
        ["X", "X", "X"],
        ["X", "X", "X"],
        ["X", "X", "X"],
    ]
    solution.solve(board)
    assert board == expected


def test_all_o_cells(solution):
    board = [
        ["O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O"],
    ]
    expected = [
        ["O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O"],
    ]
    solution.solve(board)
    assert board == expected


def test_complex_pattern(solution):
    board = [
        ["O", "X", "X", "O", "X"],
        ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"],
    ]
    expected = [
        ["O", "X", "X", "O", "X"],
        ["X", "X", "X", "X", "O"],
        ["X", "X", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"],
    ]
    solution.solve(board)
    assert board == expected


def test_diagonal_pattern(solution):
    board = [
        ["X", "O", "X", "O"],
        ["O", "X", "O", "X"],
        ["X", "O", "X", "O"],
        ["O", "X", "O", "X"],
    ]
    expected = [
        ["X", "O", "X", "O"],
        ["O", "X", "X", "X"],
        ["X", "X", "X", "O"],
        ["O", "X", "O", "X"],
    ]
    solution.solve(board)
    assert board == expected
