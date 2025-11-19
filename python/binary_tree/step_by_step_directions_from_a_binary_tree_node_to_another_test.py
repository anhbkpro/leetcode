from .step_by_step_directions_from_a_binary_tree_node_to_another import Solution
from .binary_tree_node import TreeNode


def test_step_by_step_directions_from_a_binary_tree_node_to_another():
    # Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
    # Output: "UURL"
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(4)
    assert Solution().getDirections(root, 3, 6) == "UURL"

    # Input: root = [2,1], startValue = 2, destValue = 1
    # Output: "L"
    root = TreeNode(2)
    root.left = TreeNode(1)
    assert Solution().getDirections(root, 2, 1) == "L"
