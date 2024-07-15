from .create_binary_tree_from_descriptions import Solution
from .binary_tree_node import TreeNode


def test_create_binary_tree():
    rv = Solution().createBinaryTree([[1, 2, 0], [1, 3, 1], [2, 4, 0], [2, 5, 1]])
    # The tree should look like this:
    #      1
    #     / \
    #    3   2
    #       / \
    #      5   4
    assert rv.val == 1
    assert rv.left.val == 3
    assert rv.right.val == 2
    assert rv.right.left.val == 5
    assert rv.right.right.val == 4

