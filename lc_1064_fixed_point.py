from typing import List


class Solution:
    @staticmethod
    def fixedPoint(arr: List[int]) -> int:
        lo, hi = 0, len(arr) - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == mid:
                ans = mid
                hi = mid - 1  # remove this line still works

            if arr[mid] < mid:
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
