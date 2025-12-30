from .create_binary_tree_from_descriptions import Solution


def test_create_binary_tree():
    rv = Solution().createBinaryTree([[1, 2, 0], [1, 3, 1], [2, 4, 0], [2, 5, 1]])
    # The tree should look like this:
    #      1
    #     / \
    #    3   2
    #       / \
    #      5   4
    assert rv.val == 1
    assert rv.left.val == 3
    assert rv.right.val == 2
    assert rv.right.left.val == 5
    assert rv.right.right.val == 4

    rv = Solution().createBinaryTree(
        [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
    )
    # The tree should look like this:
    #       50
    #     /   \
    #    20    80
    #   /  \   /
    #  15  17 19
    assert rv.val == 50
    assert rv.left.val == 20
    assert rv.right.val == 80
    assert rv.left.left.val == 15
    assert rv.left.right.val == 17
    assert rv.right.left.val == 19
