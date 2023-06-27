from lc_63_unique_paths_ii import uniquePathsWithObstacles


def test_unique_paths_with_obstacles():
    assert uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1
