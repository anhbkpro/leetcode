from typing import List


def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    rows, cols = len(maze), len(maze[0])
    queue = [(entrance[0], entrance[1], 0)]
    visited = set()
    visited.add((entrance[0], entrance[1]))
    while queue:
        row, col, steps = queue.pop(0)
        if (row, col) != (entrance[0], entrance[1]) and (row == 0 or row == rows - 1 or col == 0 or col == cols - 1):
            return steps
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_row, neighbor_col = row + d[0], col + d[1]
            if rows > neighbor_row >= 0 and cols > neighbor_col >= 0 and maze[neighbor_row][neighbor_col] == '.' and (neighbor_row, neighbor_col) not in visited:
                visited.add((neighbor_row, neighbor_col))
                queue.append((neighbor_row, neighbor_col, steps + 1))
    return -1


class Solution:
    pass
