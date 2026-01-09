class Solution(object):
    def subtreeWithAllDeepest(self, root):
        # Tag each node with its depth
        depth = {None: -1}

        def dfs(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        max_depth = max(depth.values())

        def answer(node):
            # Return the answer for the subtree at node
            if not node or depth[node] == max_depth:
                return node
            L = answer(node.left)
            R = answer(node.right)
            return node if L and R else L or R

        return answer(root)
