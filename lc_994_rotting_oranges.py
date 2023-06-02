from typing import List
from collections import deque


def orangesRotting(grid: List[List[int]]) -> int:
    # BFS
    # Time Complexity: O(mn)
    # Space Complexity: O(mn)
    # where m is the number of rows and n is the number of columns in grid.

    # Find the initial rotten oranges
    rotten = deque()
    fresh = 0
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if item == 2:
                rotten.append((i, j))
            elif item == 1:
                fresh += 1

    # If there are no fresh oranges, return 0
    if fresh == 0:
        return 0

    # BFS
    time = 0
    while rotten:
        # Increment the time
        time += 1

        # Get the number of rotten oranges at the current time
        num_rotten = len(rotten)

        # For each rotten orange at the current time
        for _ in range(num_rotten):
            i, j = rotten.popleft()

            # For each of the 4 neighbors
            for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                # If the neighbor is a fresh orange
                if (
                    0 <= x < len(grid)
                    and 0 <= y < len(grid[0])
                    and grid[x][y] == 1
                ):
                    # Mark it as rotten
                    grid[x][y] = 2
                    # Decrement the number of fresh oranges
                    fresh -= 1
                    # Add it to the queue
                    rotten.append((x, y))

    # If there are no fresh oranges, return the time
    if fresh == 0:
        return time - 1
    # Otherwise, return -1
    else:
        return -1


class Solution:
    pass
