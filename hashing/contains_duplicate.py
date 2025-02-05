from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class SolutionSorting:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


class SolutionHashMap:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if num in freq:
                return True
            freq[num] = 1
        return False
