from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        writer = 0
        freq = defaultdict(int)

        for reader in range(len(nums)):
            freq[nums[reader]] += 1
            if freq[nums[reader]] > 2:
                continue

            nums[writer] = nums[reader]
            writer += 1

        return writer
