from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if not s or k <= 0:
            return []

        res = []  # grouped string
        n = len(s)
        curr = 0  # starting index of each group
        # split string
        while curr < n:
            res.append(s[curr : curr + k])
            curr += k
        # try to fill in the last group
        if res:
            res[-1] += fill * (k - len(res[-1]))
        return res
