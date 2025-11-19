from .invert_binary_tree import Solution, TreeNode


def test_invert_tree():
    # Input: root = [2,1,3]
    # Output: [2,3,1]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    ans = Solution().invertTree(root)
    assert ans.val == 2
    assert ans.left.val == 3
    assert ans.right.val == 1
