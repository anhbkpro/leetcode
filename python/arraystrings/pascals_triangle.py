from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows + 1):
            tmp = [0] * i
            tmp[0] = 1
            tmp[-1] = 1
            for j in range(1, i):
                if tmp[j] == 0:
                    tmp[j] = ans[-1][j - 1] + ans[-1][j]
            ans.append(tmp)
        return ans
