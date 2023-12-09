# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, root: Optional[TreeNode], result):
        if root is None:
            return

        self.helper(root.left, result)
        result.append(root.val)
        return self.helper(root.right, result)

    @staticmethod
    def inorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result
