class Solution:
    def minPartitions(self, n: str) -> int:
        max_ch = 0
        for ch in n:
            max_ch = max(max_ch, int(ch))

        return max_ch
