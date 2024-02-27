from lc_543_diameter_of_binary_tree import Solution, TreeNode

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


def test_diameter_of_binary_tree():
    assert Solution.diameter_of_binary_tree(root) == 3
