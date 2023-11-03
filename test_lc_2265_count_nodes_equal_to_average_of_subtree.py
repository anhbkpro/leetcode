from lc_2265_count_nodes_equal_to_average_of_subtree import Solution, TreeNode
root = TreeNode(val=4)
root.left = TreeNode(val=8)
root.right = TreeNode(val=5)
root.left.left = TreeNode(val=0)
root.left.right = TreeNode(val=1)
root.right.right = TreeNode(val=6)


def test_average_of_subtree():
    assert Solution().averageOfSubtree(root=root) == 5
