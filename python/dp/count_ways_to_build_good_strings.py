from functools import lru_cache


class BaseSolution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        pass


class SolutionInterativeDP(BaseSolution):
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Use dp[i] to record to number of good strings of length i.
        dp = [1] + [0] * (high)
        mod = 10**9 + 7

        # Iterate over each length `end`.
        for end in range(1, high + 1):
            # check if the current string can be made by append zero `0`s or one `1`s.
            if end >= zero:
                dp[end] += dp[end - zero]
            if end >= one:
                dp[end] += dp[end - one]
            dp[end] %= mod

        # Add up the number of strings with each valid length [low ~ high].
        return sum(dp[low : high + 1]) % mod


class SolutionRecursiveDP(BaseSolution):
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def dp(end: int) -> int:
            if end == 0:
                return 1
            result = 0
            if end >= zero:
                result += dp(end - zero)
            if end >= one:
                result += dp(end - one)
            return result % mod

        return sum(dp(end) for end in range(low, high + 1)) % mod
