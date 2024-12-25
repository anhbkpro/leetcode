# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        q = deque([root])
        curr_max = float("-inf")
        while q:
            for _ in range(len(q)):
                item = q.popleft()
                curr_max = max(curr_max, item.val)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            ans.append(curr_max)
            curr_max = float("-inf")  # reset max val
        return ans
