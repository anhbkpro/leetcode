from typing import List


class Solution:
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def _is_in_bound(self, board: List[List[str]], row: int, col: int) -> bool:
        return 0 <= row < len(board) and 0 <= col < len(board[0])

    def _is_border_cell(self, board: List[List[str]], row: int, col: int) -> bool:
        return row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1

    def _dfs(self, board: List[List[str]], row: int, col: int, invalid_regions: set()):
        if not self._is_in_bound(board, row, col) or board[row][col] != "O":
            return

        invalid_regions.add((row, col))  # mark this as an invalid cell
        for x, y in self.dirs:
            next_row, next_col = row + x, col + y
            if (next_row, next_col) not in invalid_regions and self._is_in_bound(
                board, next_row, next_col
            ):
                self._dfs(board, next_row, next_col, invalid_regions)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        invalid_regions = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and self._is_border_cell(board, row, col):
                    invalid_regions.add((row, col))
                    self._dfs(board, row, col, invalid_regions)

        for row in range(1, len(board) - 1):
            for col in range(1, len(board[0]) - 1):
                if not (row, col) in invalid_regions and board[row][col] == "O":
                    board[row][col] = "X"
