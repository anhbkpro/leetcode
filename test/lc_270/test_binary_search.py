from src.lc_270 import binary_search


def test_closest_value():
    root = binary_search.TreeNode(4)
    root.left = binary_search.TreeNode(2)
    root.right = binary_search.TreeNode(5)
    root.left.left = binary_search.TreeNode(1)
    root.left.right = binary_search.TreeNode(3)
    assert binary_search.closestValue(root, 3.714286) == 4
    assert binary_search.closestValue(root, 3.4) == 3
