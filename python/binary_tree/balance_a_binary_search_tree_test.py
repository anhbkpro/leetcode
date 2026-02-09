from typing import List
import unittest
from .balance_a_binary_search_tree import Solution, TreeNode


def inorder_values(root: TreeNode) -> List[int]:
    if not root:
        return []
    return inorder_values(root.left) + [root.val] + inorder_values(root.right)


def height(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root: TreeNode) -> bool:
    if not root:
        return True
    return (
        abs(height(root.left) - height(root.right)) <= 1
        and is_balanced(root.left)
        and is_balanced(root.right)
    )


def build_skewed_bst(values: List[int]) -> TreeNode:
    root = None
    for v in values:
        if not root:
            root = TreeNode(v)
        else:
            cur = root
            while cur.right:
                cur = cur.right
            cur.right = TreeNode(v)
    return root


class TestBalanceBST(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertIsNone(self.solution.balanceBST(None))

    def test_single_node(self):
        root = TreeNode(1)
        balanced = self.solution.balanceBST(root)
        self.assertEqual(balanced.val, 1)
        self.assertTrue(is_balanced(balanced))

    def test_already_balanced_tree(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        balanced = self.solution.balanceBST(root)
        self.assertEqual(inorder_values(balanced), [1, 2, 3])
        self.assertTrue(is_balanced(balanced))

    def test_skewed_tree(self):
        root = build_skewed_bst([1, 2, 3, 4, 5, 6, 7])
        balanced = self.solution.balanceBST(root)

        self.assertEqual(inorder_values(balanced), [1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(is_balanced(balanced))

    def test_large_input(self):
        values = list(range(1, 101))
        root = build_skewed_bst(values)
        balanced = self.solution.balanceBST(root)

        self.assertEqual(inorder_values(balanced), values)
        self.assertTrue(is_balanced(balanced))
