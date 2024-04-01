class Solution:
    @staticmethod
    def length_of_last_word(s: str) -> int:
        p, length = len(s), 0
        while p > 0:
            p -= 1
            if s[p] != " ":
                length += 1
            elif length > 0:
                return length

        return length
