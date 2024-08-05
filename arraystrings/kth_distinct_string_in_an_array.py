from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        ans = []
        for c in arr:
            if counter[c] > 1:
                continue
            ans.append(c)
        if k > len(ans):
            return ""

        return ans[k - 1]
