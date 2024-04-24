class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n > 0 else 0
        a, b, c = 0, 1, 1
        for i in range(n-2):
            a, b, c = b, c, a + b + c
        return c


    def tribonacci_top_down(self, n: int) -> int:
        dp = {0: 0, 1: 1, 2: 1}
        def dfs(n):
            if n in dp:
                return dp[n]
            dp[n] = dfs(n-1) + dfs(n-2) + dfs(n-3)
            return dp[n]

        return dfs(n)
