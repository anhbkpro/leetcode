
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater_map = {}
        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]
            while stack and stack[-1] < num:
                stack.pop()

            if num not in greater_map:
                if stack:
                    greater_map[num] = stack[-1]
                else:
                    greater_map[num] = -1

            stack.append(num)

        ans = []
        for num in nums1:
            ans.append(greater_map[num])

        return ans
