from collections import deque


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        qs = deque()
        qt = deque()
        self.proceed_str(s, qs)
        self.proceed_str(t, qt)

        return "".join(qs) == "".join(qt)

    @staticmethod
    def proceed_str(s: str, q: deque):
        for c in s:
            print(c)
            if c is not "#":
                q.append(c)
            else:
                if q:
                    q.pop()
