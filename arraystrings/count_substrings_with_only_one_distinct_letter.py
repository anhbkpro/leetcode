class Solution:
    def countLetters(self, s: str) -> int:
        ans = 0
        left = right = 0
        for right in range(len(s)):
            if s[right] != s[left]:
                left = right
            ans += right - left + 1

        return ans
