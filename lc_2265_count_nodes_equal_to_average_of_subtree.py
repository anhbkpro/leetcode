# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.matchingSubtreeCount = None

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.matchingSubtreeCount = 0  # Initialize the count of subtrees with matching averages.
        self.averageOfSubtreeHelper(root)

        return self.matchingSubtreeCount

    def averageOfSubtreeHelper(self, root: Optional[TreeNode]) -> (int, int):
        if root is None:
            return 0, 0

        left_sum, left_count = self.averageOfSubtreeHelper(root.left)
        right_sum, right_count = self.averageOfSubtreeHelper(root.right)

        total_sum = left_sum + right_sum + root.val
        total_count = left_count + right_count + 1
        if total_sum // total_count == root.val:
            self.matchingSubtreeCount += 1

        return total_sum, total_count
