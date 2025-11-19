class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in m:
                if not stack or stack[-1] != m[c]:
                    return False
                else:
                    stack = stack[:-1]
            else:
                stack.append(c)

        if len(stack) > 0:
            return False

        return True
