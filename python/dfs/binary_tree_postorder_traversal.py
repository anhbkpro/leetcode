# Definition for a binary tree node.
from typing import List, Optional

from .tree_node import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._postorder_traversal_helper(root, result)
        return result

    def _postorder_traversal_helper(self, current_node: TreeNode, result: List[int]):
        if not current_node:
            return

        self._postorder_traversal_helper(current_node.left, result)
        self._postorder_traversal_helper(current_node.right, result)
        result.append(current_node.val)
