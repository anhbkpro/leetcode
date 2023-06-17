# Definition for a binary tree node.
from typing import Optional, List, Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closestValue(root: Optional[TreeNode], target: float) -> int:
    stack, pred = [], float('-inf')
    # To build an inorder traversal iteratively, go left as far as you can and add all nodes on the way into stack.
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        # If next element in inorder traversal
        # is closer to target, update closest
        if abs(root.val - target) < abs(pred - target):
            closest = root.val
        pred = root.val
        root = root.right
    return closest
