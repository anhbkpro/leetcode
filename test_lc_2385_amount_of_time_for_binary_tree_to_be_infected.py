from lc_2385_amount_of_time_for_binary_tree_to_be_infected import Solution, TreeNode

# root = [1,5,3,null,4,10,6,9,2], start = 3
tree = TreeNode(1)
tree.left = TreeNode(5)
tree.right = TreeNode(3)
tree.right.left = TreeNode(10)
tree.right.right = TreeNode(6)
tree.left.right = TreeNode(4)
tree.left.right.left = TreeNode(9)
tree.left.right.right = TreeNode(2)


def test_amount_of_time():
    assert Solution().amountOfTime(tree, 3) == 4
