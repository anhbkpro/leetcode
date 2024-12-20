from .reverse_odd_levels_of_binary_tree import TreeNode, Solution


def test_reverse_odd_levels():
    # Input: root = [2,3,5]
    # Output: [2,5,3]
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(5)

    result = Solution().reverseOddLevels(root=root)
    assert result.val == 2
    assert result.left.val == 5
    assert result.right.val == 3



