from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        matrix_sum = 0
        min_abs_val = float("inf")
        negative_count = 0

        for row in matrix:
            for val in row:
                matrix_sum += abs(val)
                if val < 0:
                    negative_count += 1
                min_abs_val = min(min_abs_val, abs(val))

        if negative_count % 2 != 0:
            matrix_sum -= 2 * min_abs_val

        return matrix_sum
