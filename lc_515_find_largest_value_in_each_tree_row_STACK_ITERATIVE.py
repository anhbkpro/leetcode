from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def largestValuesStackIterative(root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        stack = [(root, 0)]

        while stack:
            node, level = stack.pop()
            if not node:
                continue

            if level == len(ans):
                ans.append(node.val)
            else:
                ans[level] = max(ans[level], node.val)

            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))

        return ans
