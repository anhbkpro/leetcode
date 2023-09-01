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
            for j in range(start, end + 1):
                if j <= n:
                    dp[j] = min(dp[start] + 1, dp[j])

        return dp[n - 1]
