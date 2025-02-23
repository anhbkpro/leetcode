from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, root: TreeNode, result: List[int]):
        if not root:
            return

        self.dfs(root.left, result)
        self.dfs(root.right, result)
        result.append(root.val)
