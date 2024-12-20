# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __traverse_DFS(self, left_child, right_child, level):
        if not left_child or not right_child:
            return

        if level % 2 == 0:
            left_child.val, right_child.val = right_child.val, left_child.val
        self.__traverse_DFS(left_child.left, right_child.right, level + 1)
        self.__traverse_DFS(left_child.right, right_child.left, level + 1)

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.__traverse_DFS(root.left, root.right, 0)
        return root
