from typing import List


class Solution:
    @staticmethod
    def transpose(matrix: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ans[col][row] = matrix[row][col]

        return ans
