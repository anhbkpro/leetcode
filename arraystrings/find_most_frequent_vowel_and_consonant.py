from collections import defaultdict


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_m = defaultdict(int)
        consonan_m = defaultdict(int)
        v_max = 0
        c_max = 0
        for c in s:
            if c in "aeiou":
                vowel_m[c] += 1
                v_max = max(v_max, vowel_m[c])
            else:
                consonan_m[c] += 1
                c_max = max(c_max, consonan_m[c])
        return v_max + c_max
