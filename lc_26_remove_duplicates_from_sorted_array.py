from typing import List


class Solution:
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        writer = 0
        for reader in range(len(nums)):
            if nums[reader] != nums[writer]:
                writer += 1
                nums[writer] = nums[reader]

        return writer + 1
