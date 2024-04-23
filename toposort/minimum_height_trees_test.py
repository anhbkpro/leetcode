from toposort.minimum_height_trees import Solution


def test_find_min_height_trees():
    assert Solution().findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]) == [1]
    assert sorted(Solution().findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])) == [3, 4]
