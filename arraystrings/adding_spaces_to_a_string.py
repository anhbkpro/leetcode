from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        spaces = set(spaces)
        for i, c in enumerate(s):
            ans += (" " if i in spaces else "") + c

        return ans
