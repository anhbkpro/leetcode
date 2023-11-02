from typing import List


class Solution:
    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        n = len(nums)
        writer = 0
        for reader in range(n):
            if nums[reader] != val:
                nums[writer] = nums[reader]
                writer += 1

        return writer
