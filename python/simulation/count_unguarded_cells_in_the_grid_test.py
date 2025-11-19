from .count_unguarded_cells_in_the_grid import Solution


def test_count_unguarded_cells_in_the_grid():
    assert (
        Solution().countUnguarded(
            m=4, n=6, guards=[[0, 0], [1, 1], [2, 3]], walls=[[0, 1], [2, 2], [1, 4]]
        )
        == 7
    )
