from dfs.sum_of_distances_in_tree import Solution


def test_sum_of_distances_in_tree():
    assert Solution().sumOfDistancesInTree(
        6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    ) == [8, 12, 6, 10, 10, 10]
