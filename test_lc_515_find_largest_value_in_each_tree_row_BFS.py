from lc_515_find_largest_value_in_each_tree_row_BFS import Solution, TreeNode

root = TreeNode(val=1)
root.left = TreeNode(val=3)
root.right = TreeNode(val=2)
root.left.left = TreeNode(val=5)
root.left.right = TreeNode(val=3)
root.right.right = TreeNode(val=9)
s = Solution()

#               1
#             /   \
#            3     2
#           / \     \
#          5   3     9


def test_largest_values():
    assert s.largestValues(root=root) == [1, 3, 9]
