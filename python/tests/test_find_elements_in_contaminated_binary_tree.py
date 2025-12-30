import pytest

from binary_tree.find_elements_in_a_contaminated_binary_tree import (
    FindElements,
    TreeNode,
)


def test_find_elements_single_node():
    # Test case 1: Single node tree
    root = TreeNode(-1)
    fe = FindElements(root)
    assert fe.find(0) == True  # root value should be 0
    assert fe.find(1) == False  # no children exist
    assert fe.find(2) == False  # no children exist


def test_find_elements_complete_tree():
    # Test case 2: Complete binary tree with 3 nodes
    root = TreeNode(-1)
    root.left = TreeNode(-1)
    root.right = TreeNode(-1)
    fe = FindElements(root)

    # Check all existing values
    assert fe.find(0) == True  # root
    assert fe.find(1) == True  # left child
    assert fe.find(2) == True  # right child
    assert fe.find(3) == False  # non-existent value


def test_find_elements_left_skewed_tree():
    # Test case 3: Left-skewed tree
    root = TreeNode(-1)
    root.left = TreeNode(-1)
    root.left.left = TreeNode(-1)
    fe = FindElements(root)

    assert fe.find(0) == True  # root
    assert fe.find(1) == True  # first left child
    assert fe.find(3) == True  # second left child
    assert fe.find(2) == False  # right child (doesn't exist)
    assert fe.find(4) == False  # non-existent value


def test_find_elements_right_skewed_tree():
    # Test case 4: Right-skewed tree
    root = TreeNode(-1)
    root.right = TreeNode(-1)
    root.right.right = TreeNode(-1)
    fe = FindElements(root)

    assert fe.find(0) == True  # root
    assert fe.find(2) == True  # first right child
    assert fe.find(6) == True  # second right child
    assert fe.find(1) == False  # left child (doesn't exist)
    assert fe.find(5) == False  # non-existent value


def test_find_elements_empty_tree():
    # Test case 5: Empty tree
    root = None
    fe = FindElements(root)
    assert fe.find(0) == False  # empty tree should contain no values
