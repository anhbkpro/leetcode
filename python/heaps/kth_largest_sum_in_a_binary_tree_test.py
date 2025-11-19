from .kth_largest_sum_in_a_binary_tree import Solution, TreeNode


def test_kth_largest_sum_in_a_binary_tree():
    root = TreeNode(5)
    root.left = TreeNode(8)
    root.right = TreeNode(9)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(6)
    assert Solution().kthLargestLevelSum(root=root, k=2) == 13
