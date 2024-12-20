# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionDFS:
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


class SolutionBFS:
    def reverseOddLevels(self, root):
        if not root:
            return None  # Return None if the tree is empty.

        queue = [root]  # Start BFS with the root node.
        level = 0

        while queue:
            size = len(queue)
            current_level_nodes = []

            # Process all nodes at the current level.
            for _ in range(size):
                node = queue.pop(0)
                current_level_nodes.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse node values if the current level is odd.
            if level % 2 == 1:
                left, right = 0, len(current_level_nodes) - 1
                while left < right:
                    tmp = current_level_nodes[left].val
                    current_level_nodes[left].val = current_level_nodes[right].val
                    current_level_nodes[right].val = tmp
                    left += 1
                    right -= 1

            level += 1

        return root  # Return the modified tree root.
