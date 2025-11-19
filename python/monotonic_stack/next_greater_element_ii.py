from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        nums = nums + nums
        stack = []
        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                item = stack.pop()
                if item < n:
                    ans[item] = num
            stack.append(idx)

        return ans
