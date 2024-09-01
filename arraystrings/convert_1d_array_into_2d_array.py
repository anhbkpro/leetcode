from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        len_1d = len(original)
        if len_1d != m * n:
            return ans

        for i in range(0, len_1d, n):
            ans.append(original[i:i + n])

        return ans
