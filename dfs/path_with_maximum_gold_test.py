from dfs.path_with_maximum_gold import Solution


def test_path_with_maximum_gold():
    assert Solution().getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]) == 24
    assert (
        Solution().getMaximumGold(
            [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
        )
        == 28
    )
