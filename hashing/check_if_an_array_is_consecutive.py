from typing import Counter, List


class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        start = min(nums)
        end = start + len(nums)
        c = Counter(nums)
        for num in range(start, end):
            if num not in c:
                return False

        return True
