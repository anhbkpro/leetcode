from collections import deque
from typing import Counter


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans = ""
        candidate = sorted([c for c, f in Counter(s).items() if f >= k], reverse=True)
        q = deque(candidate)
        while q:
            curr = q.popleft()
            if len(curr) > len(ans):
                ans = curr

            for ch in candidate:
                nxt = curr + ch
                it = iter(s)
                if all(ch in it for ch in nxt * k):
                    q.append(nxt)

        return ans
