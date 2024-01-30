from typing import List


class Solution:
    @staticmethod
    def evalRPN(tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b
        }

        st = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                st.append(t)
            else:
                first = int(st.pop())
                second = int(st.pop())
                op = operations[t]
                st.append(op(second, first))

        return int(st[0])
