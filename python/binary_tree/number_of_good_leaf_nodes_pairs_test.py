from .binary_tree_node import TreeNode
from .number_of_good_leaf_nodes_pairs import Solution


def test_number_of_good_leaf_nodes_pairs():
    # Input: root = [1,2,3,null,4], distance = 3
    # Output: 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    distance = 3
    result = Solution().countPairs(root, distance)
    assert result == 1

    # Input: root = [1,2,3,4,5,6,7], distance = 3
    # Output: 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    distance = 3
    result = Solution().countPairs(root, distance)
    assert result == 2
