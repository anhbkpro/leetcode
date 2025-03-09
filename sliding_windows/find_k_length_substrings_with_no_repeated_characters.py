from collections import Counter


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        cnt = Counter(s[:k])
        if len(cnt) == k:
            ans += 1
        for right in range(k, len(s)):
            cnt[s[right]] += 1
            cnt[s[right - k]] -= 1
            if cnt[s[right - k]] == 0:
                del cnt[s[right - k]]
            if len(cnt) == k:
                ans += 1
            left += 1

        return ans
