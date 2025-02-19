from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        p_left, p_right = 0, len(height) - 1
        max_area = 0
        while p_left < p_right:
            width = p_right - p_left
            min_height = min(height[p_left], height[p_right])
            max_area = max(max_area, width * min_height)

            # Move the pointer with smaller height
            if height[p_left] <= height[p_right]:
                p_left += 1
            else:
                p_right -= 1

        return max_area
