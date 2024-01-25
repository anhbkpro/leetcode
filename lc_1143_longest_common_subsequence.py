class Solution:
    @staticmethod
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        r, c = len(text1), len(text2)
        # Make a grid of 0's with len(text2) + 1 columns 
        # and len(text1) + 1 rows.
        dp_grid = [[0] * (c + 1) for _ in range(r + 1)]

        # Iterate up each column, starting from the last one.
        for col in reversed(range(c)):
            for row in reversed(range(r)):
                # If the corresponding characters for this cell are the same...
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                # Otherwise they must be different...
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])

        # The original problem's answer is in dp_grid[0][0]. Return it.
        return dp_grid[0][0]
