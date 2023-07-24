from lc_1644_lowest_common_ancestor_of_a_binary_tree_ii import Solution, TreeNode


def test_lowest_common_ancestor():
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    p = root.left
    q = root.right
    assert Solution.lowestCommonAncestor(root=root, p=p, q=q).val == 3
