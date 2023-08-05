from lc_95_unique_binary_search_trees_ii import Solution, TreeNode


root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, None)))


def test_all_possible_bst():
    expected = [TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, None))),
                TreeNode(1, None, TreeNode(3, TreeNode(2, None, None), None)),
                TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)),
                TreeNode(3, TreeNode(1, None, TreeNode(2, None, None)), None),
                TreeNode(3, TreeNode(2, TreeNode(1, None, None), None), None)]

    expected = [str(node) for node in expected]
    result = Solution().allPossibleBST(1, 3, {})
    for node in result:
        assert str(node) in expected
