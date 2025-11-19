class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for c in s:
            flag = True
            while stk and c == "*":
                stk.pop()
                flag = False
                break

            if flag:
                stk.append(c)

        return "".join(stk)
