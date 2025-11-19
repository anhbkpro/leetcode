from .binary_tree_postorder_traversal import Solution, TreeNode


def test_postorder_traversal():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    assert Solution().postorderTraversal(root) == [3, 2, 1]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert Solution().postorderTraversal(root) == [4, 5, 2, 6, 7, 3, 1]

    root = TreeNode(1)
    assert Solution().postorderTraversal(root) == [1]

    assert Solution().postorderTraversal(None) == []
