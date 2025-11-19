from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [0] * len(nums)
        less = 0
        greater = len(nums) - 1
        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                ans[less] = nums[i]
                less += 1
            if nums[j] > pivot:
                ans[greater] = nums[j]
                greater -= 1
        while less <= greater:
            ans[less] = pivot
            less += 1

        return ans
