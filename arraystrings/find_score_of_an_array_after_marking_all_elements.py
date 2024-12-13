from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums_sorted = sorted((num, idx) for idx, num in enumerate(nums))
        ans = 0
        for num, idx in nums_sorted:
            if nums[idx] == -1:
                continue

            ans += num
            nums[idx] = -1
            if idx - 1 >= 0:
                nums[idx - 1] = -1
            if idx + 1 <= len(nums) - 1:
                nums[idx + 1] = -1
        return ans
