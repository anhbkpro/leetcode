class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != "."]
        symbols = [(-1, "L")] + symbols + [(len(dominoes), "R")]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            elif x > y:  # RL
                for k in range(i + 1, j):
                    # Replace cmp function which doesn't exist in Python 3
                    if k - i < j - k:
                        ans[k] = "L"
                    elif k - i > j - k:
                        ans[k] = "R"
                    else:
                        ans[k] = "."

        return "".join(ans)
