class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_len = 0
        freq = {}
        while right < len(s):
            if s[right] in freq:
                # Move left pointer to the right of the last occurrence of the character
                left = max(left, freq[s[right]] + 1)

            freq[s[right]] = right
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
