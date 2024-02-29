# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


class Solution:
    @staticmethod
    def is_even_odd_tree(root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if root.val % 2 == 0:
            return False

        def is_monotonic(nodes: list, is_even_level: bool) -> bool:
            if not nodes:
                return True

            is_increasing = True
            is_decreasing = True

            if len(nodes) == 1:
                if is_even_level:
                    return nodes[0] % 2 == 1
                return nodes[0] % 2 == 0

            for i in range(len(nodes) - 1):
                if nodes[i] == nodes[i + 1]:
                    return False

                if is_even_level:
                    if nodes[i] % 2 == 0 or nodes[i + 1] % 2 == 0:
                        return False
                else:
                    if nodes[i] % 2 == 1 or nodes[i + 1] % 2 == 1:
                        return False

                if nodes[i] < nodes[i + 1]:
                    is_decreasing = False
                if nodes[i] > nodes[i + 1]:
                    is_increasing = False
            if is_even_level:
                return is_increasing

            return not is_even_level and is_decreasing

        cur_level = 0
        dq = deque([root])
        while dq:
            number_of_nodes = len(dq)
            cur_data_at_level = []

            while number_of_nodes > 0:
                number_of_nodes -= 1
                node = dq.popleft()
                cur_data_at_level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            if not is_monotonic(cur_data_at_level, cur_level % 2 == 0):
                return False

            cur_level += 1

        return True
