from typing import List


class BaseSolution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return False


class Solution(BaseSolution):
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        check = nums[0] % 2
        for i in range(1, len(nums)):
            if nums[i] % 2 == check:
                return False
            check = not check

        return True


class SolutionModuloComparisons(BaseSolution):
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False

        return True


class SolutionBitwiseOperations(BaseSolution):
    def isArraySpecial(self, nums):
        # Iterate through indexes 0 to n - 1
        for index in range(len(nums) - 1):

            # Compare the parities using bitwise operations
            if ((nums[index] & 1) ^ (nums[index + 1] & 1)) == 0:

                # If the two adjacent numbers have the same parity, return False
                return False

        # Return True if no pair of adjacent numbers with the same parity are found
        return True