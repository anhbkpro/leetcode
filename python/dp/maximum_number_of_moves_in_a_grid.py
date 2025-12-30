from dataclasses import dataclass
from typing import List


@dataclass
class GridPosition:
    row: int
    col: int


class GridMoveSolver:
    """Class to solve maximum possible moves in a grid with given constraints"""

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.dp = [[-1] * self.cols for _ in range(self.rows)]
        self.directions = [-1, 0, 1]  # Up-right, right, down-right

    def is_valid_position(self, pos: GridPosition) -> bool:
        """Check if a position is within grid boundaries"""
        return 0 <= pos.row < self.rows and 0 <= pos.col < self.cols

    def is_valid_move(self, current: GridPosition, next_pos: GridPosition) -> bool:
        """Check if move is valid based on grid value constraints"""
        if not self.is_valid_position(next_pos):
            return False
        return (
            self.grid[next_pos.row][next_pos.col] > self.grid[current.row][current.col]
        )

    def get_next_positions(self, current: GridPosition) -> List[GridPosition]:
        """Get all possible next positions from current position"""
        next_positions = []
        next_col = current.col + 1

        for dir in self.directions:
            next_row = current.row + dir
            next_pos = GridPosition(next_row, next_col)

            if self.is_valid_move(current, next_pos):
                next_positions.append(next_pos)

        return next_positions

    def find_max_moves_from_position(self, pos: GridPosition) -> int:
        """Find maximum possible moves from a given position using DFS with memoization"""
        # Return memoized result if available
        if self.dp[pos.row][pos.col] != -1:
            return self.dp[pos.row][pos.col]

        max_moves = 0
        # Get all possible next positions
        next_positions = self.get_next_positions(pos)

        # Recursively find max moves for each valid next position
        for next_pos in next_positions:
            moves = 1 + self.find_max_moves_from_position(next_pos)
            max_moves = max(max_moves, moves)

        # Memoize result
        self.dp[pos.row][pos.col] = max_moves
        return max_moves

    def solve(self) -> int:
        """Find maximum possible moves starting from first column"""
        max_moves = 0

        # Try starting from each position in first column
        for row in range(self.rows):
            start_pos = GridPosition(row, 0)
            moves = self.find_max_moves_from_position(start_pos)
            max_moves = max(max_moves, moves)

        return max_moves


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        solver = GridMoveSolver(grid)
        return solver.solve()
