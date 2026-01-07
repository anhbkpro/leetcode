from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        # 1. Compute total sum of tree
        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        total = total_sum(root)
        self.max_product = 0

        # 2. Compute subtree sums and update max product
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            subtree = node.val + left + right

            # consider cutting above this subtree
            self.max_product = max(self.max_product, subtree * (total - subtree))

            return subtree

        dfs(root)
        return self.max_product % MOD
