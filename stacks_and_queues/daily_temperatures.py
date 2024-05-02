from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # decreasing monotonic
        ans = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            current_temp = temperatures[i]
            while stack and stack[-1][0] <= current_temp:
                stack.pop()

            if not stack:
                # no warmer day
                ans[i] = 0
            else:
                # found warmer day
                next_warmer_day = stack[-1][1]
                ans[i] = next_warmer_day - i

            stack.append([current_temp, i])

        return ans
