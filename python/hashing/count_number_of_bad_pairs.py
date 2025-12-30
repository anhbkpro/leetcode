from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        bad_paids = 0
        for i, num in enumerate(nums):
            diff = num - i
            good_pairs = freq[diff]
            bad_paids += i - good_pairs
            freq[diff] += 1

        return bad_paids
