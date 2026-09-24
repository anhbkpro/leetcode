from typing import List


class Solution:
    def get_digit_sum(self, num: int) -> int:
        total = 0
        while num:
            num, digit = divmod(num, 10)
            total += digit
        return total

    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i == self.get_digit_sum(num):
                return i
        return -1
