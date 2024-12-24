from .minimum_number_of_operations_to_sort_a_binary_tree_by_level import (
    Solution,
    TreeNode,
)


def test_minimum_operations():
    # root = [1,3,2,7,6,5,4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    assert Solution().minimumOperations(root=root) == 0
