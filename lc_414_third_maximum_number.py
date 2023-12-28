from cmath import inf
from typing import List


class Solution:
    @staticmethod
    def thirdMax(nums: List[int]) -> int:
        first = second = third = -inf
        for num in nums:
            if first == num or second == num or third == num:
                continue

            if first <= num:
                third = second
                second = first
                first = num
            elif second <= num:
                third = second
                second = num
            elif third <= num:
                third = num

        if third == -inf:
            return first

        return third
