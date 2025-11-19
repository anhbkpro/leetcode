from .delete_nodes_and_return_forest import Solution
from .binary_tree_node import TreeNode


def test_del_nodes():
    # Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
    # Output: [[1,2,null,4],[6],[7]]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    to_delete = [3, 5]
    result = Solution().delNodes(root, to_delete)
    assert len(result) == 3
    assert result[0].val == 6
    assert result[1].val == 7
    assert result[2].val == 1
