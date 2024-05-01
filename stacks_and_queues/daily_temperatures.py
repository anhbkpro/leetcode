from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # decreasing monotonic
        rv = []
        ans = []
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            while stack and stack[-1][0] <= temp:
                stack.pop()

            if not stack:
                # no warmer day
                rv.append(0)
            else:
                # found warmer day
                rv.append(stack[-1][1] - i)
            stack.append([temp, i])

        for i in range(len(rv) - 1, -1, -1):
            ans.append(rv[i])

        return ans
