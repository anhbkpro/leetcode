# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: Optional[TreeNode]) -> int:
    return dfs(root)


class Solution:
    pass


def dfs(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    if root.left is None:
        return 1 + dfs(root.right)
    elif root.right is None:
        return 1 + dfs(root.left)

    return 1 + min(dfs(root.left), dfs(root.right))
