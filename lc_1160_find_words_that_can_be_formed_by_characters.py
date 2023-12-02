from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def countCharacters(words: List[str], chars: str) -> int:
        freq = Counter(chars)
        ans = 0
        for word in words:
            word_freq = Counter(word)
            good = True
            for c, f in word_freq.items():
                if c not in freq or f > freq[c]:
                    good = False
                    break

            if good:
                ans += len(word)

        return ans
