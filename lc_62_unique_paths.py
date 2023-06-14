def unique_paths(m: int, n: int) -> int:
    d = [[1] * n for _ in range(m)]

    for col in range(1, m):
        for row in range(1, n):
            d[col][row] = d[col - 1][row] + d[col][row - 1]

    return d[m - 1][n - 1]


def my_unique_paths(m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[m - 1][n - 1] = 1
    for r in reversed(range(m)):
        for c in reversed(range(n)):
            print(f"r = {r}; c = {c}")
            if r == m - 1 and c == n - 1:
                continue
            else:
                dp[r][c] = dp[min(r + 1, m - 1)][c] + dp[r][min(c + 1, n - 1)]
            print(f"({r}, {c}) = {dp[r][c]}")
    return dp[0][0]


class Solution:
    pass
