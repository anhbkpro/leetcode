from .maximum_depth_of_binary_tree import Solution, TreeNode


def test_maximum_depth_of_binary_tree():
    # root = [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().maxDepth(root)
    assert result == 3

    # root = [1,null,2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    result = Solution().maxDepth(root)
    assert result == 2
