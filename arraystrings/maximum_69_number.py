class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        result = []
        used = False
        for c in num_str:
            if c == "6" and not used:
                result.append("9")
                used = True
            else:
                result.append(c)
        return int("".join(result))
