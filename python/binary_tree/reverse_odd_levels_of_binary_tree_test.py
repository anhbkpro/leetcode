from .reverse_odd_levels_of_binary_tree import TreeNode, SolutionDFS, SolutionBFS


def test_reverse_odd_levels():
    # Input: root = [2,3,5]
    # Output: [2,5,3]
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(5)

    dfs_result = SolutionDFS().reverseOddLevels(root=root)
    assert dfs_result.val == 2
    assert dfs_result.left.val == 5
    assert dfs_result.right.val == 3

    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    bfs_result = SolutionBFS().reverseOddLevels(root=root)
    assert bfs_result.val == 2
    assert bfs_result.left.val == 5
    assert bfs_result.right.val == 3
