class Solution:
    @staticmethod
    def character_replacement(s: str, k: int) -> int:
        def count_replacements(most_char_repeating_freq: int, window_len: int) -> int:
            return window_len - most_char_repeating_freq

        ans = 1
        l, r = 0, 0
        freq = {}
        max_freq = 0
        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])
            while count_replacements(max_freq, r - l + 1) > k:
                freq[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)
            r += 1

        return ans
