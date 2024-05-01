from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_m = Counter("balloon")
        text_m = Counter(text)
        count = len(text)
        for c in balloon_m:
            if c not in text_m:
                return 0

            count = min(count, text_m[c] // balloon_m[c])

        return count
