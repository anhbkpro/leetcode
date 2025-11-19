from collections import Counter
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        n = len(nums)
        if len(freq) == n:
            return 0

        ops = 0
        for i in range(len(nums)):
            if i % 3 == 0:
                if len(freq) == n - i:
                    return ops
                ops += 1

            freq[nums[i]] -= 1
            if freq[nums[i]] == 0:
                del freq[nums[i]]

        return ops
