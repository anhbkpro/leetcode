class Solution:
    def max_depth(self, s: str) -> int:
        stack = []
        ans = 0
        for c in s:
            if c == "(":
                stack.append(c)
                ans = max(ans, len(stack))
            elif c == ")" and stack:
                stack.pop()

        return ans
