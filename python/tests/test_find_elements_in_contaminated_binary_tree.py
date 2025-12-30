from binary_tree.find_elements_in_a_contaminated_binary_tree import (
    FindElements,
    TreeNode,
)


def test_find_elements_single_node():
    # Test case 1: Single node tree
    root = TreeNode(-1)
    fe = FindElements(root)
    assert fe.find(0)  # root value should be 0
    assert not fe.find(1)  # no children exist
    assert not fe.find(2)  # no children exist


def test_find_elements_complete_tree():
    # Test case 2: Complete binary tree with 3 nodes
    root = TreeNode(-1)
    root.left = TreeNode(-1)
    root.right = TreeNode(-1)
    fe = FindElements(root)

    # Check all existing values
    assert fe.find(0)  # root
    assert fe.find(1)  # left child
    assert fe.find(2)  # right child
    assert not fe.find(3)  # non-existent value


def test_find_elements_left_skewed_tree():
    # Test case 3: Left-skewed tree
    root = TreeNode(-1)
    root.left = TreeNode(-1)
    root.left.left = TreeNode(-1)
    fe = FindElements(root)

    assert fe.find(0)  # root
    assert fe.find(1)  # first left child
    assert fe.find(3)  # second left child
    assert not fe.find(2)  # right child (doesn't exist)
    assert not fe.find(4)  # non-existent value


def test_find_elements_right_skewed_tree():
    # Test case 4: Right-skewed tree
    root = TreeNode(-1)
    root.right = TreeNode(-1)
    root.right.right = TreeNode(-1)
    fe = FindElements(root)

    assert fe.find(0)  # root
    assert fe.find(2)  # first right child
    assert fe.find(6)  # second right child
    assert not fe.find(1)  # left child (doesn't exist)
    assert not fe.find(5)  # non-existent value


def test_find_elements_empty_tree():
    # Test case 5: Empty tree
    root = None
    fe = FindElements(root)
    assert not fe.find(0)  # empty tree should contain no values
