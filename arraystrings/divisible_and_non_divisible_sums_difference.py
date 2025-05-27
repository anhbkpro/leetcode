class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num = 0
        for i in range(n + 1):
            if i % m == 0:
                num -= i
            else:
                num += i
        return num
