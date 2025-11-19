from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes_cnt = 0
        left = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes_cnt += 1
            while zeroes_cnt > k:
                if nums[left] == 0:
                    zeroes_cnt -= 1
                left += 1

            ans = max(ans, right - left + 1)
        return ans
