from bisect import bisect_right
from typing import List


class Solution:
    @staticmethod
    def minOperations(nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))

        for i in range(len(new_nums)):
            left = new_nums[i]
            right = left + n - 1
            j = bisect_right(new_nums, right)  # find the index after the greatest number <= right
            # for example if new_nums = [2, 3, 4, 7, ->12<-, 15, 44] and right = 9, then j = 4
            count = j - i  # calculate the number of elements already in our range
            ans = min(ans, n - count)

        return ans
