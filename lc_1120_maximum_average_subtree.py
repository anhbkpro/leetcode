# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_avg = 0

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.helper(root)
        return self.max_avg

    def helper(self, root):
        if not root:
            return 0, 0
        left_sum, left_count = self.helper(root.left)
        right_sum, right_count = self.helper(root.right)
        total_sum = left_sum + right_sum + root.val
        total_count = left_count + right_count + 1
        self.max_avg = max(self.max_avg, total_sum / total_count)
        return total_sum, total_count
