# Lowest Common Ancestor of Deepest Leaves

This document explains the function `lcaDeepestLeaves` which finds the lowest common ancestor (LCA) of the deepest leaves in a binary tree.

## Code

```python
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 0, None
            left = dfs(root.left)
            right = dfs(root.right)
            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root
        return dfs(root)[1]
```

## Simple Explanation

This code finds the lowest common ancestor of all nodes at the deepest level of a binary tree. In other words, it identifies the lowest node that is an ancestor to all the deepest leaf nodes.

### How It Works

1. The algorithm uses a depth-first search (DFS) approach to explore the tree
2. For each node, the `dfs` helper function returns two pieces of information:
   - The depth of the node (distance from the root)
   - The lowest common ancestor of the deepest leaves in the subtree

3. The DFS function follows these rules:
   - For empty nodes: return depth 0 and no ancestor (None)
   - For each node: recursively call DFS on left and right children
   - Compare the depths from both sides:
     - If the left subtree has deeper leaves, use its result
     - If the right subtree has deeper leaves, use its result
     - If both sides have leaves at the same depth, the current node is the LCA

4. The final result is the ancestor part of the DFS result from the root

## Example Walkthrough

Let's trace through the execution with this example tree:

```
    1
   / \
  2   3
 /     \
4       5
       /
      6
```

### Step-by-Step Execution

1. Start at the root (node 1) and call `dfs(1)`

2. For node 1:
   - Process left subtree: `dfs(2)`
   - Process right subtree: `dfs(3)`

3. For node 2:
   - Process left: `dfs(4)` → Returns `(1, 4)` (depth 1, node 4)
   - Process right: `dfs(None)` → Returns `(0, None)` (depth 0, no node)
   - Since left is deeper, return `(2, 4)` (depth 2, node 4)

4. For node 3:
   - Process left: `dfs(None)` → Returns `(0, None)` (depth 0, no node)
   - Process right: `dfs(5)` → Continues below...

5. For node 5:
   - Process left: `dfs(6)` → Returns `(1, 6)` (depth 1, node 6)
   - Process right: `dfs(None)` → Returns `(0, None)` (depth 0, no node)
   - Since left is deeper, return `(2, 6)` (depth 2, node 6)

6. Back to node 3:
   - Left result: `(0, None)`
   - Right result: `(2, 6)`
   - Since right is deeper, return `(3, 6)` (depth 3, node 6)

7. Finally, back to node 1:
   - Left result: `(2, 4)`
   - Right result: `(3, 6)`
   - Since right is deeper, return `(4, 6)` (depth 4, node 6)

8. The final result is `dfs(root)[1]` = node 6

In this example, node 6 is the deepest leaf (at depth 3), and since it's the only node at that depth, it is also its own lowest common ancestor.

If there were multiple nodes at the deepest level on both sides of the tree, the LCA would be their common ancestor (the root of the smallest subtree containing all deepest leaves).
