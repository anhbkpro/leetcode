class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = right = 0
        char_to_next_idx = {}
        while right < len(s):
            if s[right] in char_to_next_idx:
                left = max(left, char_to_next_idx[s[right]])
            max_len = max(max_len, right - left + 1)
            char_to_next_idx[s[right]] = right + 1
            right += 1
        return max_len
