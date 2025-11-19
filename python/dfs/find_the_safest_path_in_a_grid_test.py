from dfs.find_the_safest_path_in_a_grid import Solution


def test_find_the_safest_path():
    assert Solution().maximumSafenessFactor(grid=[[0, 0, 1], [0, 0, 0], [0, 0, 0]]) == 2
    assert (
        Solution().maximumSafenessFactor(
            grid=[[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
        )
        == 2
    )
