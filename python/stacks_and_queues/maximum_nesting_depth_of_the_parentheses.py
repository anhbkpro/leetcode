class Solution:
    def max_depth(self, s: str) -> int:
        ans, stack = 0, []
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                stack.pop()
            ans = max(ans, len(stack))
        return ans
