class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return self.depthFirstSearch(n, k, 0)

    def depthFirstSearch(self, n: int, k: int, rootVal: int) -> int:
        if n == 1:
            return rootVal

        total_nodes = 2 ** (n - 1)

        if k <= total_nodes / 2:
            next_root_val = 0 if rootVal == 0 else 1
            return self.depthFirstSearch(n - 1, k, next_root_val)
        else:
            next_root_val = 1 if rootVal == 0 else 0
            return self.depthFirstSearch(n - 1, k - (total_nodes / 2), next_root_val)
