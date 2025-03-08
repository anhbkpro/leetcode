from collections import Counter


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if len(blocks) < k:
            return -1

        cnt = Counter(blocks[:k])
        ans = cnt.get("W", 0)
        for r in range(k, len(blocks)):
            cnt[blocks[r]] += 1
            cnt[blocks[r - k]] -= 1
            ans = min(ans, cnt.get("W", 0))

        return ans
