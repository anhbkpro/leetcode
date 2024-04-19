from dfs.island_perimeter import Solution


def test_island_perimeter():
    assert Solution().islandPerimeter([
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]) == 16
    assert Solution().islandPerimeter([[1]]) == 4
    assert Solution().islandPerimeter([[1, 0]]) == 4
