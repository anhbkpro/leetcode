from lc_606_construct_string_from_binary_tree import Solution, TreeNode

s = Solution()
root = TreeNode(val=1)
root.left = TreeNode(val=2)
root.right = TreeNode(val=3)
root.left.left = TreeNode(val=4)


def test_tree2str():
    assert s.tree2str(root=root) == "1(2(4))(3)"
