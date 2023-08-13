class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        def numberOfWays(i: int) -> int:
            if i <= 2:
                return i

            if i in dp:
                return dp[i]

            dp[i] = numberOfWays(i - 1) + numberOfWays(i - 2)
            return dp[i]

        dp = {}
        return numberOfWays(n)
