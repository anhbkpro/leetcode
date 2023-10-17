from lc_1361_validate_binary_tree_nodes import Solution


def test_validate_binary_tree_nodes():
    assert Solution.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]) is True
    assert Solution.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]) is False
