from lc_1214_two_sum_bsts import twoSumBSTs
from lc_1161_maximum_level_sum_of_a_binary_tree import TreeNode


def test_two_sum_bsts():
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)

    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(3)

    assert twoSumBSTs(root1, root2, 5) is True
