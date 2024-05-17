from dfs.delete_leaves_with_a_given_value import Solution, TreeNode


def test_delete_leaves_with_a_given_value():
    # Input: root = [1,2,3,2,null,2,4], target = 2
    # Output: [1,null,3,null,4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    Solution().removeLeafNodes(root, 2)
    assert root.val == 1
    assert root.left is None
    assert root.right.val == 3
    assert root.right.left is None
    assert root.right.right.val == 4
