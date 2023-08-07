from typing import List


class Solution:
    @staticmethod
    def searchMatrix(matrix: List[List[int]], target: int) -> bool:
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


def find_row(last_cols: List[int], target: int) -> int:
    lo, hi = 0, len(last_cols) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if last_cols[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return hi
