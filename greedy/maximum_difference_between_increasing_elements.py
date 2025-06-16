from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num = float("inf")
        ans = float("-inf")
        for num in nums:
            min_num = min(min_num, num)
            if min_num < num:
                ans = max(ans, num - min_num)
        return ans if ans != float("-inf") else -1
