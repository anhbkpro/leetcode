import collections
from typing import List


class Solution:
    @staticmethod
    def findMatrix(nums: List[int]) -> List[List[int]]:
        f = collections.Counter(nums)
        ans = []
        sub_len = max(f.values())
        print(sub_len)
        for i in range(sub_len):
            sub_arr = []
            for j in f:
                if f[j] > 0:
                    f[j] -= 1
                    sub_arr.append(j)
            ans.append(sub_arr)
        return ans