from typing import List


# My Solution
class Solution:
    @staticmethod
    def search_matrix(matrix: List[List[int]], target: int) -> bool:
        last_cols = []
        for r in matrix:
            last_cols.append(r[-1])

        print(last_cols)
        row = find_row(last_cols, target)
        print(row)

        items = matrix[row]
        lo, hi = 0, len(items) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if items[mid] == target:
                return True
            elif items[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False

    @staticmethod
    def search_matrix_lc(matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # binary search
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False


def find_row(last_cols: List[int], target: int) -> int:
    lo, hi = 0, len(last_cols) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if last_cols[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return hi
