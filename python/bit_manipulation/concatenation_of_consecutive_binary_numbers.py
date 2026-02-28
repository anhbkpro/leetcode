class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 0

        for i in range(1, n + 1):
            shift = i.bit_length()   # number of bits needed for i
            ans = ((ans << shift) + i) % MOD

        return ans
