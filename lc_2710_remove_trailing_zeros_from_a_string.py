def removeTrailingZeros(num: str) -> str:
    while num[-1] == "0":
        num = num[:-1]
    return num


class Solution:
    pass
