from typing import List


class Solution:
    @staticmethod
    def evalRPN(tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        st = []
        for t in tokens:
            if t not in operations:
                st.append(int(t))
            else:
                first = st.pop()
                second = st.pop()
                op = operations[t]
                st.append(op(second, first))

        return st.pop()
