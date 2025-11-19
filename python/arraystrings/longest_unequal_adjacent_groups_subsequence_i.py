from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        stk = []
        for i, g in enumerate(groups):
            if not stk or groups[stk[-1]] != g:
                stk.append(i)
        ans = []
        for i in stk:
            ans.append(words[i])

        return ans
