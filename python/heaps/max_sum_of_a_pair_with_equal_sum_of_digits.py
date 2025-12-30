from heapq import heappop, heappush
from typing import List


class Solution:
    def _calculate_digit_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_groups = [[] for _ in range(82)]
        ans = -1
        for i, num in enumerate(nums):
            digit_sum = self._calculate_digit_sum(num)
            heappush(digit_sum_groups[digit_sum], num)

            if len(digit_sum_groups[digit_sum]) > 2:
                heappop(digit_sum_groups[digit_sum])

        for min_heap in digit_sum_groups:
            if len(min_heap) != 2:
                continue

            first = heappop(min_heap)
            second = heappop(min_heap)
            ans = max(ans, first + second)

        return ans
