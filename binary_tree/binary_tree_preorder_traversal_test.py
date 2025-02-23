import unittest
from binary_tree.binary_tree_preorder_traversal import Solution, TreeNode


class TestBinaryTreePreorderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Test preorder traversal of an empty tree"""
        self.assertEqual(self.solution.preorderTraversal(None), [])

    def test_single_node(self):
        """Test preorder traversal of a tree with a single node"""
        root = TreeNode(1)
        self.assertEqual(self.solution.preorderTraversal(root), [1])

    def test_complete_binary_tree(self):
        """Test preorder traversal of a complete binary tree
        Tree structure:
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        expected = [1, 2, 4, 5, 3, 6, 7]
        self.assertEqual(self.solution.preorderTraversal(root), expected)

    def test_left_skewed_tree(self):
        """Test preorder traversal of a left-skewed tree
        Tree structure:
            1
           /
          2
         /
        3
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)

        expected = [1, 2, 3]
        self.assertEqual(self.solution.preorderTraversal(root), expected)

    def test_right_skewed_tree(self):
        """Test preorder traversal of a right-skewed tree
        Tree structure:
        1
         \
          2
           \
            3
        """
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)

        expected = [1, 2, 3]
        self.assertEqual(self.solution.preorderTraversal(root), expected)

    def test_unbalanced_tree(self):
        """Test preorder traversal of an unbalanced tree
        Tree structure:
            1
           / \
          2   3
         /     \
        4       5
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)

        expected = [1, 2, 4, 3, 5]
        self.assertEqual(self.solution.preorderTraversal(root), expected)


if __name__ == "__main__":
    unittest.main()
