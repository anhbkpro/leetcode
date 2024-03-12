from typing import List


class Solution:
    def min_sub_array_len(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        window_sum = 0
        min_len = len(nums) + 1
        while right < len(nums):
            window_sum += nums[right]
            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1
            right += 1

        return min_len if min_len != len(nums) + 1 else 0
