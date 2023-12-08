from lc_1120_maximum_average_subtree import Solution, TreeNode

s = Solution()
root = TreeNode(val=5)
root.left = TreeNode(val=6)
root.right = TreeNode(val=1)


def test_maximum_average_subtree():
    assert s.maximumAverageSubtree(root=root) == 6.0
