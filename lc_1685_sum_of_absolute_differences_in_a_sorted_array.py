from typing import List


class Solution:
    @staticmethod
    def getSumAbsoluteDifferences(nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        left_sum = 0
        ans = []

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            left_count = i
            right_count = n - 1 - i

            left_total = left_count * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]

            ans.append(left_total + right_total)
            left_sum += nums[i]

        return ans
