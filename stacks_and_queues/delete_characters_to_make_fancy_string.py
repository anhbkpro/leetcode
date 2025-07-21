class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        ans = []
        for i in range(len(s)):
            c = s[i]
            if len(ans) > 1 and c == ans[-1] and c == ans[-2]:
                continue
            ans.append(c)

        return "".join(ans)
