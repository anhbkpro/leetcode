from functools import lru_cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(nums, n, subset_sum) -> bool:
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            # skip or take an element
            result = dfs(nums, n - 1, subset_sum - nums[n - 1]) or dfs(
                nums, n - 1, subset_sum
            )
            return result

        total = sum(nums)
        if total % 2:
            return False

        subset_sum = total // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, subset_sum)
