from lc_530_minimum_absolute_difference_in_bst import get_minimum_difference, TreeNode
root = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)), right=TreeNode(val=6))


def test_get_minimum_difference():
    assert get_minimum_difference(root=root) == 1
