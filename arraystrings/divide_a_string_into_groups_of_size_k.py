from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = [s[i - k + 1 : (i + 1)] for i in range(len(s)) if (i + 1) % k == 0]
        start = 0
        if len(ans) > 0:
            start = len(ans[0]) * len(ans)
        if start < len(s):
            final = s[start:]
            final += fill * (k - len(final))
            ans.append(final)

        return ans
