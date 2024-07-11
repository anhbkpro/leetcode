class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ")":
                stack.append(c)
            elif stack and stack[-1] == "(":
                # for case () - non characters inside
                stack.pop()
            else:
                t = c
                tmp = []
                while stack and t != "(":
                    tmp.append(stack.pop())
                    if stack:
                        t = stack[-1]

                if stack:
                    stack.pop()
                for n in tmp:
                    stack.append(n)

        return "".join(stack)

