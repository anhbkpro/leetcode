from typing import List


class Solution:
    @staticmethod
    def missing_number(nums: List[int]) -> int:
        n = len(nums)
        ans = n
        for i in range(n):
            # XOR operation: a ^ b ^ b = a ^ 0 = a
            ans ^= i ^ nums[i]

        return ans
