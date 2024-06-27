class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if len(word) > len(sequence):
            return 0

        ans, i = 0, 0
        word_len = len(word)
        curr_max = 0
        while i < len(sequence):
            if sequence[i:word_len + i] == word:
                curr_max += 1
                i += word_len
            elif curr_max > 0:
                i = i - word_len + 1
                ans = max(ans, curr_max)
                curr_max = 0
            else:
                i += 1

        return max(ans, curr_max)
