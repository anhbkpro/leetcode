import lc_270_closest_binary_search_tree_value as closest_value


def test_closest_value():
    root = closest_value.TreeNode(4)
    root.left = closest_value.TreeNode(2)
    root.right = closest_value.TreeNode(5)
    root.left.left = closest_value.TreeNode(1)
    root.left.right = closest_value.TreeNode(3)
    assert closest_value.closestValue(root, 3.714286) == 4
    assert closest_value.closestValue(root, 3.4) == 3
