class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
                    ')': '(',
                    '}': '{',
                    ']': '[',
                }
        stack = []
        for c in s:
            if c in pairs:
                if not stack or pairs[c] != stack[-1]:
                    return False
                stack.pop() # don not use stack = stack[:-1] creates a new list every time you pop → unnecessary O(n) work.
            else:
                stack.append(c)

        return len(stack) == 0