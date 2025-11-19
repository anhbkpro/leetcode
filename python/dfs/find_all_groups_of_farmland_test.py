from dfs.find_all_groups_of_farmland import Solution


def test_find_farmland():
    assert Solution().find_farmland([[1, 0, 0], [0, 1, 1], [0, 1, 1]]) == [
        [0, 0, 0, 0],
        [1, 1, 2, 2],
    ]
    assert Solution().find_farmland([[1, 1], [1, 1]]) == [[0, 0, 1, 1]]
    assert Solution().find_farmland(
        [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
    ) == [[0, 0, 1, 1], [2, 2, 3, 3]]
