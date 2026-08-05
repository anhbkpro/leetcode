from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for x, y in zip(nums, nums[1:]):
            ans.extend(range(x + 1, y))
        return ans
