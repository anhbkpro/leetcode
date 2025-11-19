from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        longest_window = 0
        zero_count = 0
        for right in range(len(nums)):
            zero_count += nums[right] == 0

            # Shrink the window until the count of zero's
            # is less than or equal to 1.
            while zero_count > 1:
                zero_count -= nums[left] == 0
                left += 1

            longest_window = max(longest_window, right - left)
        return longest_window
