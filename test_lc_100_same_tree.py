from lc_100_same_tree import Solution, TreeNode


def test_is_same_tree():
    assert Solution().is_same_tree(None, None) is True
    assert Solution().is_same_tree(None, TreeNode(1)) is False
    assert Solution().is_same_tree(TreeNode(1), None) is False
    assert Solution().is_same_tree(TreeNode(1), TreeNode(1)) is True
