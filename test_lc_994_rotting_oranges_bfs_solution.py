from lc_994_rotting_oranges_bfs_solution import orangesRotting


def test_oranges_rotting():
    assert orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
