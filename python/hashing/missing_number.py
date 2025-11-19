from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums)
        for number in range(n + 1):
            if number not in num_set:
                return number

        return -1
