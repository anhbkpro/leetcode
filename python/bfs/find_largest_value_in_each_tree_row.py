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
        queue = deque([root])
        while queue:
            curr_len = len(queue)
            curr_max = float("-inf")

            for _ in range(curr_len):
                item = queue.popleft()
                curr_max = max(curr_max, item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            ans.append(curr_max)

        return ans
