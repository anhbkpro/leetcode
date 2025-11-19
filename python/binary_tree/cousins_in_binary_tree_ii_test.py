from .cousins_in_binary_tree_ii import Solution
from .binary_tree_node import TreeNode


def test_cousins_in_binary_tree_ii():
    tree = TreeNode(3)
    tree.left = TreeNode(1)
    tree.right = TreeNode(2)
    Solution().replaceValueInTree(root=tree)
    assert tree.val == 0
    assert tree.left.val == 0
    assert tree.right.val == 0
