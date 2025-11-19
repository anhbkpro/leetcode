class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for c in s:
            sub_str = ""
            flag = True
            while stk and c == "]":
                top = stk[-1]
                if top != "[":
                    sub_str = stk.pop() + sub_str
                elif top == "[":
                    stk.pop()
                    # Before [ is a number
                    # Watch out this constraints: All the integers in s are in the range [1, 300].
                    num = ""
                    while stk and stk[-1].isnumeric():
                        num = stk.pop() + num
                    new_str = int(num) * sub_str
                    stk.append(new_str)
                    flag = False
                    break

            if flag:
                stk.append(c)

        return "".join(stk)
