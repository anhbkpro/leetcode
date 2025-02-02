from typing import List


class Solution:
    def to_str(self, nums: List[int]) -> str:
        return "-".join(str(num) for num in nums)

    def check(self, nums: List[int]) -> bool:
        sorted_dash_separated = self.to_str(sorted(nums))
        dup_nums_dash_separated = self.to_str(nums + nums)
        return sorted_dash_separated in dup_nums_dash_separated
