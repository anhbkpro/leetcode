from typing import List


class BaseSolution:
    def check(self, nums: List[int]) -> bool:
        pass


class Solution(BaseSolution):
    def to_str(self, nums: List[int]) -> str:
        return "-".join(str(num) for num in nums)

    def check(self, nums: List[int]) -> bool:
        sorted_dash_separated = self.to_str(sorted(nums))
        dup_nums_dash_separated = self.to_str(nums + nums)
        return sorted_dash_separated in dup_nums_dash_separated


class SolutionFindSmallestElement(BaseSolution):
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        inversion_count = 0

        # For every pair, count the number of inversions.
        for index in range(1, n):
            if nums[index] < nums[index - 1]:
                inversion_count += 1

        # Also check between the last and the first element due to rotation
        if nums[0] < nums[n - 1]:
            inversion_count += 1

        return inversion_count <= 1
