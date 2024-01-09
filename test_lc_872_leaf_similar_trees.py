from lc_872_leaf_similar_trees import *

tree1 = TreeNode(3)
tree1.left = TreeNode(5)
tree1.right = TreeNode(1)
tree1.left.left = TreeNode(6)
tree1.left.right = TreeNode(2)
tree1.left.right.left = TreeNode(7)
tree1.left.right.right = TreeNode(4)
tree1.right.left = TreeNode(9)
tree1.right.right = TreeNode(8)

tree2 = TreeNode(3)
tree2.left = TreeNode(5)
tree2.right = TreeNode(1)
tree2.left.left = TreeNode(6)
tree2.left.right = TreeNode(7)
tree2.right.left = TreeNode(4)
tree2.right.right = TreeNode(2)
tree2.right.right.left = TreeNode(9)
tree2.right.right.right = TreeNode(8)


def test_leaf_similar():
    assert Solution.leafSimilar(tree1, tree2) is True
