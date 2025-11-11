class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            count = self.countzeroesones(s)
            for zeroes in range(m, count[0] - 1, -1):
                for ones in range(n, count[1] - 1, -1):
                    dp[zeroes][ones] = max(1 + dp[zeroes - count[0]][ones - count[1]],
                                           dp[zeroes][ones])

        return dp[m][n]

    def countzeroesones(self, s):
        c = [0, 0]
        for char in s:
            c[int(char)] += 1
        return c
