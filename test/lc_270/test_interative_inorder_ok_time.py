from src.lc_270 import interative_inorder_ok_time


def test_closest_value():
    root = interative_inorder_ok_time.TreeNode(4)
    root.left = interative_inorder_ok_time.TreeNode(2)
    root.right = interative_inorder_ok_time.TreeNode(5)
    root.left.left = interative_inorder_ok_time.TreeNode(1)
    root.left.right = interative_inorder_ok_time.TreeNode(3)
    assert interative_inorder_ok_time.closestValue(root, 3.714286) == 4
    assert interative_inorder_ok_time.closestValue(root, 3.4) == 3


