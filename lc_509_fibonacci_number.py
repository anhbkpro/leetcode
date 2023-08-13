class Solution:
    @staticmethod
    def fib(n: int) -> int:
        dp = {}

        def numberOfWays(i):
            if i <= 1:
                return i
            if i in dp:
                return dp[i]
            dp[i] = numberOfWays(i - 1) + numberOfWays(i - 2)
            return dp[i]

        return numberOfWays(n)
