class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_set = set(word)
        result = set()
        for w in word:
            if w.lower() in char_set and w.upper() in char_set:
                result.add(w.lower())

        return len(result)
