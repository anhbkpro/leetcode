from .maximum_number_of_moves_in_a_grid import Solution


def test_maximum_number_of_moves_in_a_grid():
    assert (
        Solution().maxMoves(
            grid=[[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
        )
        == 3
    )
    assert Solution().maxMoves(grid=[[3, 2, 4], [2, 1, 9], [1, 1, 7]]) == 0
