from python.binary_tree.binary_tree_node import TreeNode


from collections import deque
from typing import Any, List, Optional, Tuple

from .binary_tree_node import TreeNode


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Sets to track unique children and parents
        children = set[Any]()
        parents = set[Any]()
        # Dictionary to store parent to children relationships
        parentToChildren = dict[Any, List[Tuple[Any, int]]]()

        # Build graph from parent to child, and add nodes to sets
        for d in descriptions:
            parent, child, isLeft = d
            parents.add(parent)
            parents.add(child)
            children.add(child)
            if parent not in parentToChildren:
                parentToChildren[parent] = list[Tuple[Any, int]]()
            parentToChildren[parent].append((child, isLeft))

        # Find the root node by checking which node is
        # in parents but not in children
        for parent in parents.copy():
            if parent in children:
                parents.remove(parent)

        root = TreeNode(next(iter(parents)))

        # Starting from root, use BFS to construct binary tree
        queue = deque[TreeNode]([root])

        while queue:
            parent = queue.popleft()
            # Iterate over children of current parent
            for childValue, isLeft in parentToChildren.get(parent.val, []):
                child = TreeNode(childValue)
                queue.append(child)
                # Attach child node to its parent based on isLeft flag
                if isLeft == 1:
                    parent.left = child
                else:
                    parent.right = child

        return root
