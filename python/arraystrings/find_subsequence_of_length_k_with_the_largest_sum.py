from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        vals = [[i, nums[i]] for i in range(n)]
        vals.sort(key=lambda x: -x[1])  # sort value in descending order
        vals = sorted(vals[:k])
        res = [val for _, val in vals]
        return res
