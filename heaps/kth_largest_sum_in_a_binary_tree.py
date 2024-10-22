import heapq
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        heap = []
        while q:
            nodes_num = len(q)
            row_sum = 0
            for _ in range(nodes_num):
                current_node = q.popleft()
                row_sum += current_node.val
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)

            heapq.heappush(heap, row_sum)
            if len(heap) > k:
                heapq.heappop(heap)

        if len(heap) < k:
            return -1

        max_heap = []
        for count in heap:
            heapq.heappush(max_heap, -count)

        last = -1
        while len(max_heap) > 0:
            last = -heapq.heappop(max_heap)

        return last
