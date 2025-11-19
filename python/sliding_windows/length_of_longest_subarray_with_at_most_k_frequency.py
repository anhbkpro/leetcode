from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def max_subarray_length(nums: List[int], k: int) -> int:
        if k < 1:
            return 0

        left = 0
        ans = 0
        number_freq_map = Counter()
        for right in range(len(nums)):
            number_freq_map[nums[right]] += 1
            while number_freq_map[nums[right]] > k:
                number_freq_map[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
