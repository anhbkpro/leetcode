from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def majority_element(nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        for i in range(n):
            freq[nums[i]] += 1

        for (k, v) in freq.items():
            if v > n / 2:
                return k

        return -1

    @staticmethod
    def majority_element_boyer_moore_voting(nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            count += (1 if candidate == num else -1)

        return candidate
