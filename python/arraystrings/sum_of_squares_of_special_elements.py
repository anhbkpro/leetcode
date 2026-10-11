from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(
            nums[k - 1] ** 2
            for k in range(1, n + 1)
            if n % k == 0
        )