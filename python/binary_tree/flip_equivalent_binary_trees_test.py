from .flip_equivalent_binary_trees import Solution, TreeNode


def test_flip_equivalent_binary_trees():
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(8)
    root1.right.left = TreeNode(6)

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(6)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(5)
    root2.right.right.left = TreeNode(8)
    root2.right.right.right = TreeNode(7)

    assert Solution().flipEquiv(root1=root1, root2=root2) is True
