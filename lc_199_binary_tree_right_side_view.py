from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    queue = [root]
    res = []
    while queue:
        size = len(queue)
        for i in range(size):
            # pop from left
            node = queue.pop(0)
            # if it is the last node at this level
            if i == size - 1:
                res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res


class Solution:
    pass
