from lc_1660_correct_a_binary_tree import Solution, TreeNode


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = root.right


def test_correct_binary_tree():
    result = Solution().correctBinaryTree(root)
    assert result is not None
    assert result.val == 1
    assert result.left is None
    assert result.right.val == 3
