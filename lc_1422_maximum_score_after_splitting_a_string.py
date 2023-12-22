class Solution:
    @staticmethod
    def maxScore(s: str) -> int:
        zero_left = 1 if s[0] == "0" else 0
        one_left = 0 if s[0] == "0" else 1
        one_total = s.count("1")
        ans = 0
        for i in range(1, len(s)):
            ans = max(ans, zero_left + one_total - one_left)
            zero_left += 1 if s[i] == "0" else 0
            one_left += 1 if s[i] == "1" else 0

        return ans
