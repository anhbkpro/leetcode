from lc_94_binary_tree_inorder_traversal import Solution, TreeNode
s = Solution()
root = TreeNode(val=1)
root.right = TreeNode(val=2)
root.right.left = TreeNode(val=3)


def test_inorder_traversal():
    assert s.inorder_traversal(root=root) == [1, 3, 2]
    assert s.inorder_traversal_iterative(root=root) == [1, 3, 2]
