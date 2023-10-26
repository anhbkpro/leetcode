from collections import deque
from typing import List


class Solution:
    @staticmethod
    def trap(height: List[int]) -> int:
        stack = deque()
        ans = 0
        current = 0
        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                distance = current - stack[-1] - 1
                bounded_height = min(height[stack[-1]], height[current]) - height[top]
                ans += bounded_height * distance

            stack.append(current)
            current += 1

        return ans
