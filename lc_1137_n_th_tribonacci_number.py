def tribonacci(n: int) -> int:
    if n < 3:
        return 1 if n > 0 else 0
    a, b, c = 0, 1, 1
    for i in range(n-2):
        a, b, c = b, c, a + b + c
    return c


class Solution:
    pass
