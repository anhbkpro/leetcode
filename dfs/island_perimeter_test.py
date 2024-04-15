from dfs.island_perimeter import Solution


def test_island_perimeter():
    assert Solution().island_perimeter([
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]) == 16
    assert Solution().island_perimeter([[1]]) == 4
    assert Solution().island_perimeter([[1, 0]]) == 4
