from lc_1609_even_odd_tree import Solution, TreeNode



def test_is_even_odd_tree():
    assert (
        Solution.is_even_odd_tree(
            TreeNode(
                1,
                TreeNode(4, TreeNode(1), TreeNode(3)),
                TreeNode(2, None, None)
            )
        )
        is True
    )
