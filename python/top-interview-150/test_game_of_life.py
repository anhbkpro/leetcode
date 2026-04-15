import pytest
from game_of_life import Solution


@pytest.fixture
def solver():
    return Solution()


def test_example_case(solver):
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]

    expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    solver.gameOfLife(board)
    assert board == expected


def test_all_dead(solver):
    board = [[0, 0], [0, 0]]

    expected = [[0, 0], [0, 0]]

    solver.gameOfLife(board)
    assert board == expected


def test_all_live(solver):
    board = [[1, 1], [1, 1]]

    expected = [[1, 1], [1, 1]]

    solver.gameOfLife(board)
    assert board == expected


def test_single_cell_live(solver):
    board = [[1]]
    expected = [[0]]  # dies (underpopulation)

    solver.gameOfLife(board)
    assert board == expected


def test_single_cell_dead(solver):
    board = [[0]]
    expected = [[0]]

    solver.gameOfLife(board)
    assert board == expected


def test_blinker_oscillator(solver):
    # classic oscillator
    board = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

    expected = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]

    solver.gameOfLife(board)
    assert board == expected


def test_block_still_life(solver):
    # stable structure
    board = [[1, 1], [1, 1]]

    expected = [[1, 1], [1, 1]]

    solver.gameOfLife(board)
    assert board == expected


@pytest.mark.parametrize(
    "board, expected",
    [
        ([[1, 0, 0], [0, 1, 1], [1, 1, 0]], [[0, 1, 0], [0, 0, 1], [1, 1, 1]]),
        ([[0, 1], [1, 1]], [[1, 1], [1, 1]]),
    ],
)
def test_various_cases(solver, board, expected):
    solver.gameOfLife(board)
    assert board == expected
