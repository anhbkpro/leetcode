import unittest

from .find_largest_value_in_each_tree_row import Solution, TreeNode


class TestLargestValues(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Test case for empty tree"""
        self.assertEqual(self.solution.largestValues(None), [])

    def test_single_node(self):
        """Test case for tree with single node"""
        root = TreeNode(1)
        self.assertEqual(self.solution.largestValues(root), [1])

    def test_complete_binary_tree(self):
        """Test case for a complete binary tree
           Tree structure:
                1
               / \
              3   2
             / \   \
            5   3   9
        """
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(9)

        expected = [1, 3, 9]  # Max values at each level
        self.assertEqual(self.solution.largestValues(root), expected)

    def test_left_skewed_tree(self):
        """Test case for a left-skewed tree
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
        self.assertEqual(self.solution.largestValues(root), expected)

    def test_right_skewed_tree(self):
        """Test case for a right-skewed tree
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
        self.assertEqual(self.solution.largestValues(root), expected)

    def test_negative_values(self):
        """Test case for tree with negative values
           Tree structure:
                -1
               /  \
             -2   -3
        """
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)

        expected = [-1, -2]  # Max value at each level
        self.assertEqual(self.solution.largestValues(root), expected)

    def test_mixed_values(self):
        """Test case for tree with mixed positive and negative values
           Tree structure:
                1
               / \
              -2  3
             /    \
            4     -5
        """
        root = TreeNode(1)
        root.left = TreeNode(-2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(-5)

        expected = [1, 3, 4]
        self.assertEqual(self.solution.largestValues(root), expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
