from typing import List


class Solution:
    @staticmethod
    def rearrange_array(nums: List[int]) -> List[int]:
        positives = [num for num in nums if num >= 0]
        negatives = [num for num in nums if num < 0]
        for i in range(len(positives)):
            nums[2 * i] = positives[i]
            nums[2 * i + 1] = negatives[i]

        return nums