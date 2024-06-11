class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] != c and stack[-1].upper() == c.upper():
                stack = stack[:-1]
            else:
                stack.append(c)

        return "".join(stack)
