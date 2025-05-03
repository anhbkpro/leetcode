from typing import List, Tuple

LEFT_SYMBOL: str = "L"
RIGHT_SYMBOL: str = "R"
DOT_SYMBOL: str = "."


class Solution:
    def push_dominoes(self, dominoes: str) -> str:
        symbols: List[Tuple[int, str]] = self._get_symbols(dominoes)
        ans: List[str] = list(dominoes)
        self._fill_dominoes(ans, symbols)
        return "".join(ans)

    def _get_symbols(self, dominoes: str) -> List[Tuple[int, str]]:
        symbols: List[Tuple[int, str]] = [
            (i, x) for i, x in enumerate(dominoes) if x != DOT_SYMBOL
        ]
        symbols = [(-1, LEFT_SYMBOL)] + symbols + [(len(dominoes), RIGHT_SYMBOL)]
        return symbols

    def _fill_dominoes(self, ans: List[str], symbols: List[Tuple[int, str]]) -> None:
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                self._fill_range(ans, i + 1, j, x)
            elif x > y:
                self._fill_rl(ans, i, j)

    def _fill_range(self, ans: List[str], start: int, end: int, symbol: str) -> None:
        for k in range(start, end):
            ans[k] = symbol

    def _fill_rl(self, ans: List[str], i: int, j: int) -> None:
        for k in range(i + 1, j):
            if k - i < j - k:
                ans[k] = RIGHT_SYMBOL
            elif k - i > j - k:
                ans[k] = LEFT_SYMBOL
            else:
                ans[k] = DOT_SYMBOL


if __name__ == "__main__":
    solution = Solution()
    print(solution.push_dominoes("R.....L"))
