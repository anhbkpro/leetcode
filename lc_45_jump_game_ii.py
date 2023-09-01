from typing import List


class Solution:
    @staticmethod
    def jump(nums: List[int]) -> int:
        inf = int(1e9)
        n = len(nums)
        dp = [inf] * (n + 1)
        dp[0] = 0
        end = nums[0]
        for i in range(n):
            start = i
            end = i + nums[i]
            for i in range(start, end + 1):
                if i <= n:
                    dp[i] = min(dp[start] + 1, dp[i])

        return dp[n - 1]
