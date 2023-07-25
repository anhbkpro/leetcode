from typing import List


class Solution:
    @staticmethod
    def peak_index_in_mountain_array(arr: List[int]) -> int:
        lo, hi = 1, len(arr) - 1
        while lo < hi:
            m = (lo + hi) // 2
            if arr[m] < arr[m + 1]:
                lo = m + 1
            else:
                hi = m

        return lo
