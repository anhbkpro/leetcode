import collections
from collections import Counter

class Solution:
    @staticmethod
    def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
        n = len(s)
        max_size = 0
        freq = Counter()

        left = 0
        for right in range(n):
            freq[s[right]] += 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            max_size = max(max_size, right - left + 1)

        return max_size
