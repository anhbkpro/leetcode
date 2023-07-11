from lc_863_all_nodes_distance_k_in_binary_tree import distanceK, TreeNode
head = TreeNode(3)
head.left = TreeNode(5)
head.right = TreeNode(1)
head.left.left = TreeNode(6)
head.left.right = TreeNode(2)
head.right.left = TreeNode(0)
head.right.right = TreeNode(8)
head.left.right.left = TreeNode(7)
head.left.right.right = TreeNode(4)


def test_distance_k():
    res = distanceK(head, head.left, 2)
    assert sorted(res) == [1, 4, 7]
