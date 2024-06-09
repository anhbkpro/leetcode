from .add_one_row_to_tree import Solution, TreeNode


def test_add_one_row():
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(5)

    rv = s.addOneRow(root, 1, 2)
    assert rv.val == 4
    assert rv.left.val == 1
    assert rv.right.val == 1
    assert rv.left.left.val == 2
    assert rv.right.right.val == 6
