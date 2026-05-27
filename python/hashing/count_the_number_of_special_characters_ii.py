from collections import defaultdict


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        result = set()
        upper_char_to_idx = defaultdict(int)
        word_set = set(word)
        to_remove = set()

        for i, w in enumerate(word):
            if w.lower() in word_set and w.upper() in word_set:
                if w == w.upper() and w not in upper_char_to_idx:
                    upper_char_to_idx[w.lower()] = i
                if (
                    w in upper_char_to_idx
                    and w == w.lower()
                    and i > upper_char_to_idx[w]
                ):
                    to_remove.add(w.lower())
                    continue
                result.add(w.lower())
        for c in to_remove:
            result.remove(c)

        return len(result)

    def count_special_chars(self, word: str) -> int:
        last_lower: dict[str, int] = {}
        first_upper: dict[str, int] = {}

        for i, c in enumerate(word):
            if c.islower():
                last_lower[c] = i  # keep updating → captures last position
            elif c.isupper() and c.lower() not in first_upper:
                first_upper[c.lower()] = i  # only set once → captures first position

        return sum(
            1
            for c, last in last_lower.items()
            if c in first_upper and last < first_upper[c]
        )
