from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def is_leaf(node: Optional[TreeNode]) -> bool:
            return node.left is None and node.right is None

        def helper(node: Optional[TreeNode]) -> bool:
            if node is None:
                return True

            if is_leaf(node):
                return True if node.val == 1 else False

            return helper(node.left) and helper(node.right) if node.val == 3 else helper(node.left) or helper(node.right)

        return helper(root)
