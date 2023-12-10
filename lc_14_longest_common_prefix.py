from typing import List


class Solution:
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        ans = strs[0]
        for i in range(1, len(strs)):
            ans = ans[:min(len(ans), len(strs[i]))]
            for j in range(len(strs[i])):
                if j < len(ans) and strs[i][j] != ans[j]:
                    ans = ans[:j]
                    break

        return ans
