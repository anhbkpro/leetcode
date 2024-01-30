from typing import List


class Solution:
    @staticmethod
    def evalRPN(tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                s.append(t)
            else:
                first = int(s.pop())
                second = int(s.pop())
                res = 0
                if t == "+":
                    res = first + second
                elif t == "-":
                    res = second - first
                elif t == "*":
                    res = first * second
                elif second != 0:
                    res = second / first
                s.append(res)

        return int(s[0])
