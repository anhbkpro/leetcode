class Solution:
    @staticmethod
    def hammingWeight(n: int) -> int:
        sum = 0
        while n != 0:
            sum += 1
            n &= (n - 1)

        return sum
