from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        p_left = p_right = 0
        ans = float("-inf")
        window_sum = 0
        while p_right < len(nums):
            window_sum += nums[p_right]
            if p_right - p_left + 1 == k:
                ans = max(ans, window_sum / k)
                window_sum -= nums[p_left]
                p_left += 1

            p_right += 1
        return ans
