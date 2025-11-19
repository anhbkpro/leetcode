from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        tmp_arr = sorted(arr)
        size = len(arr)
        m = {}
        continuous_index = 1
        for i in range(size):
            if tmp_arr[i] in m:
                continue
            m[tmp_arr[i]] = continuous_index
            continuous_index += 1

        ans = [None] * size
        for i in range(size):
            ans[i] = m[arr[i]]
        return ans
