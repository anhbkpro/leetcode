class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True

        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord("a")] += 1
        odd_count = len([c for c in freq if c % 2])

        return odd_count <= k
