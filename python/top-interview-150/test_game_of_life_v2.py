import pytest
from game_of_life import Solution


@pytest.mark.parametrize(
    "board, expected",
    [
        (
            [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
        ),
        ([[1, 1], [1, 0]], [[1, 1], [1, 1]]),
        ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
        (
            [[1]],
            [[0]],  # single live cell dies
        ),
        (
            [[0]],
            [[0]],  # stays dead
        ),
    ],
)
def test_game_of_life(board, expected):
    sol = Solution()
    sol.gameOfLife(board)
    assert board == expected
