from lc_111_minimum_depth_of_binary_tree import minDepth, TreeNode


def test_min_depth():
    assert minDepth(None) == 0
    assert minDepth(TreeNode(1, None, None)) == 1
    assert minDepth(TreeNode(1, TreeNode(2, None, None), None)) == 2
    assert minDepth(TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))) == 2
