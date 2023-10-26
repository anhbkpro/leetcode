from typing import List


class Solution:
    @staticmethod
    def maxArea(height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            distance = right - left
            current_area = distance * min(height[left], height[right])
            area = max(area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area
