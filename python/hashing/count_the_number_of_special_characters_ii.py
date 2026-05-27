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
