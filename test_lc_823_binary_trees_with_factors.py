from lc_823_binary_trees_with_factors import Solution


def test_num_factored_binary_trees():
    assert Solution.numFactoredBinaryTrees([2, 4]) == 3
    assert Solution.numFactoredBinaryTrees([2, 4, 5, 10]) == 7
