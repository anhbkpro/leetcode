from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        """
        Count the number of servers that can communicate with at least one other server.
        A server can communicate with another server if they are in the same row or column.

        Args:
            grid: A matrix where grid[i][j] is 1 if there is a server at (i,j), or 0 if empty

        Returns:
            The number of servers that can communicate with at least one other server
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        servers_in_row = [0] * rows  # Count of servers in each row
        servers_in_col = [0] * cols  # Count of servers in each column
        server_positions = []  # Store positions of all servers

        # First pass: Count servers in each row and column
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    servers_in_row[i] += 1
                    servers_in_col[j] += 1
                    server_positions.append((i, j))

        # Second pass: Count servers that can communicate
        connected_servers = sum(
            1 for i, j in server_positions
            if servers_in_row[i] > 1 or servers_in_col[j] > 1
        )

        return connected_servers
