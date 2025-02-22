import unittest
from binary_tree.recover_a_tree_from_preorder_traversal import Solution, TreeNode


class TestRecoverFromPreorder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertTreeEqual(self, expected: TreeNode, actual: TreeNode):
        if expected is None and actual is None:
            return True
        if expected is None or actual is None:
            return False

        return (
            expected.val == actual.val
            and self.assertTreeEqual(expected.left, actual.left)
            and self.assertTreeEqual(expected.right, actual.right)
        )

    def test_basic_tree(self):
        # Test case: "1-2--3--4-5--6--7"
        #       1
        #     /   \
        #    2     5
        #   / \   / \
        #  3   4 6   7
        traversal = "1-2--3--4-5--6--7"
        result = self.solution.recoverFromPreorder(traversal)

        # Create expected tree
        expected = TreeNode(1)
        expected.left = TreeNode(2)
        expected.right = TreeNode(5)
        expected.left.left = TreeNode(3)
        expected.left.right = TreeNode(4)
        expected.right.left = TreeNode(6)
        expected.right.right = TreeNode(7)

        self.assertTreeEqual(expected, result)

    def test_single_node(self):
        traversal = "1"
        result = self.solution.recoverFromPreorder(traversal)
        expected = TreeNode(1)
        self.assertTreeEqual(expected, result)

    def test_left_skewed_tree(self):
        # Test case: "1-2--3"
        #     1
        #    /
        #   2
        #  /
        # 3
        traversal = "1-2--3"
        result = self.solution.recoverFromPreorder(traversal)

        expected = TreeNode(1)
        expected.left = TreeNode(2)
        expected.left.left = TreeNode(3)

        self.assertTreeEqual(expected, result)

    def test_multi_digit_values(self):
        # Test case: "10-20--30--40"
        #      10
        #     /
        #    20
        #   /  \
        #  30   40
        traversal = "10-20--30--40"
        result = self.solution.recoverFromPreorder(traversal)

        expected = TreeNode(10)
        expected.left = TreeNode(20)
        expected.left.left = TreeNode(30)
        expected.left.right = TreeNode(40)

        self.assertTreeEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
