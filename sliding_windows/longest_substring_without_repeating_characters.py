from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = start = 0
        last_index_map = defaultdict(int)
        n = len(s)
        for end in range(n):
            c = s[end]
            if c in last_index_map:
                start = max(start, last_index_map[c] + 1)
            ans = max(ans, end - start + 1)
            last_index_map[c] = end
        return ans
