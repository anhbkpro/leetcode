from lc_450_delete_node_in_a_bst import Solution, TreeNode

solution = Solution()


def test_delete_node():
    root = TreeNode(val=5, left=TreeNode(val=3, left=TreeNode(val=2), right=TreeNode(val=4)),
                    right=TreeNode(val=6, right=TreeNode(val=7)))
    result = solution.deleteNode(root, key=3)
    assert result is not None
