from typing import List


class Solution:

    # Get the maximum area in a histogram given its heights
    def leetcode84(self, heights):
        stack = [-1]

        max_area = 0
        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return max_area


    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix: return 0

        max_area = 0
        # builds a histogram for each row instead of each column
        # for each histogram (row); we based on the LeetCode 84 solution to calculate the max area
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                # update the state of this row's histogram using the last row's histogram
                # by keeping track of the number of consecutive ones
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

            # update max_area with the maximum area from this row's histogram
            print(f"histogram in row {i}: {dp}")
            max_area = max(max_area, self.leetcode84(dp))
        return max_area