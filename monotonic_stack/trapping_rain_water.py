from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        current = 0
        st = []
        while current < len(height):
            while st and height[current] > height[st[-1]]:
                top = st.pop()
                if len(st) == 0:
                    break
                distance = current - st[-1] - 1
                bounded_height = min(height[current], height[st[-1]]) - height[top]
                ans += distance * bounded_height

            st.append(current)
            current += 1

        return ans
