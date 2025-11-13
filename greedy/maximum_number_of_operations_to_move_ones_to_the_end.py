class Solution:
    def maxOperations(self, s: str) -> int:
        one = 0
        ans = 0
        for i, c in enumerate(s):
            if c == "1":
                if i > 0 and s[i - 1] == "0":
                    ans += one
                one += 1
            if i == len(s) - 1 and s[i] == "0":
                ans += one
        return ans
