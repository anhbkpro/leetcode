from dfs.evaluate_boolean_binary_tree import Solution, TreeNode


def test_evaluate_boolean_binary_tree():
    # Input: root = [2,1,3,null,null,0,1]
    # Output: true
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    assert Solution().evaluateTree(root) is True

    # Input: root = [0]
    # Output: false
    root = TreeNode(0)
    assert Solution().evaluateTree(root) is False
