from lc_1161_maximum_level_sum_of_a_binary_tree import max_level_sum, TreeNode


def test_max_level_sum():
    node = TreeNode(val=1, left=TreeNode(val=7, left=TreeNode(val=7), right=TreeNode(val=-8)), right=TreeNode(val=0))
    assert max_level_sum(node) == 2
