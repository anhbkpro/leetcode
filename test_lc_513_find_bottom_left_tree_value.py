from lc_513_find_bottom_left_tree_value import Solution, TreeNode


def test_find_bottom_left_value():
    assert Solution.find_bottom_left_value(TreeNode(2, TreeNode(1), TreeNode(3))) == 1
    assert (
        Solution.find_bottom_left_value(
            TreeNode(
                1,
                TreeNode(2, TreeNode(4), None),
                TreeNode(3, TreeNode(5, TreeNode(7), None), TreeNode(6)),
            )
        )
        == 7
    )
