from collections import deque


class TreeNode:
    """
    This represents a node of a tree has value inside and has at most 2 children, left and right
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def find_bottom_left_value(root):
        queue = deque()
        current = root
        queue.append(current)

        while queue:
            current = queue.popleft()

            if current.right:
                queue.append(current.right)

            if current.left:
                queue.append(current.left)

        return current.val

