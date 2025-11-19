class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            st = str(i)
            if len(st) % 2:
                continue
            n = len(st) // 2
            first_half = st[:n]
            second_half = st[n:]
            first_half_sum = sum([int(c) for c in first_half])
            second_half_sum = sum([int(c) for c in second_half])
            if first_half_sum == second_half_sum:
                ans += 1
        return ans
