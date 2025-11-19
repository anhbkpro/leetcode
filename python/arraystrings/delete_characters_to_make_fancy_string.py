class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        ans = []
        prev_1st, prev_2nd = s[:2]
        ans.extend([prev_1st, prev_2nd])
        for i in range(2, len(s)):
            if s[i] == prev_2nd and prev_2nd == prev_1st:
                prev_1st = s[i - 1]
                prev_2nd = s[i]
                continue
            ans.append(s[i])
            prev_1st = s[i - 1]
            prev_2nd = s[i]

        return "".join(ans)
