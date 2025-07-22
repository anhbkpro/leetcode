from collections import defaultdict
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window_sum = 0
        left = right = 0
        freq = defaultdict(int)
        ans = 0
        while right < len(nums):
            window_sum += nums[right]
            freq[nums[right]] += 1
            while freq[nums[right]] > 1:
                window_sum -= nums[left]
                freq[nums[left]] -= 1
                if freq[nums[left]] <= 0:
                    del freq[nums[left]]
                left += 1
            ans = max(ans, window_sum)
            right += 1

        return ans
