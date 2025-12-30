from typing import List


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        def binary_search(array: List[int], target: int) -> bool:
            left, r = 0, len(array) - 1
            while left <= r:
                m = (left + r) // 2
                if array[m] == target:
                    return True
                elif array[m] < target:
                    left = m + 1
                else:
                    r = m - 1

            return False

        s = []
        for num in arrays[0]:
            valid = True
            for array in arrays[1:]:
                if not binary_search(array, num):
                    valid = False
            if valid and (len(s) == 0 or num > s[-1]):
                s.append(num)

        return s
