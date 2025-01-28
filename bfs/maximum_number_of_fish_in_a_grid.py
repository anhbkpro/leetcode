class SolutionDFS:
    # Helper function to count the number of fishes in a connected component
    def calculate_fishes(self, grid, visited, row, col):
        # Check boundary conditions, water cells, or already visited cells
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or grid[row][col] == 0
            or visited[row][col]
        ):
            return 0

        # Mark the current cell as visited
        visited[row][col] = True

        # Accumulate the fish count from the current cell and its neighbors
        return (
            grid[row][col]
            + self.calculate_fishes(grid, visited, row, col + 1)
            + self.calculate_fishes(grid, visited, row, col - 1)
            + self.calculate_fishes(grid, visited, row + 1, col)
            + self.calculate_fishes(grid, visited, row - 1, col)
        )

    def findMaxFish(self, grid):
        rows, cols = len(grid), len(grid[0])
        max_fish_count = 0

        # A 2D list to track visited cells
        visited = [[False] * cols for _ in range(rows)]

        # Iterate through all cells in the grid
        for row in range(rows):
            for col in range(cols):
                # Start a DFS for unvisited land cells (fish available)
                if grid[row][col] > 0 and not visited[row][col]:
                    max_fish_count = max(
                        max_fish_count,
                        self.calculate_fishes(grid, visited, row, col),
                    )

        # Return the maximum fish count found
        return max_fish_count


class SolutionBFS:
    # Function to perform BFS and count fishes in the connected component
    def count_fishes(self, grid, visited, row, col):
        num_rows = len(grid)
        num_cols = len(grid[0])
        fish_count = 0
        q = [(row, col)]
        visited[row][col] = True

        # Directions for exploring up, down, left, right
        row_directions = [0, 0, 1, -1]
        col_directions = [1, -1, 0, 0]

        # BFS traversal
        while q:
            row, col = q.pop(0)
            fish_count += grid[row][col]

            # Exploring all four directions
            for i in range(4):
                new_row = row + row_directions[i]
                new_col = col + col_directions[i]
                if (
                    0 <= new_row < num_rows
                    and 0 <= new_col < num_cols
                    and grid[new_row][new_col]
                    and not visited[new_row][new_col]
                ):
                    q.append((new_row, new_col))
                    visited[new_row][new_col] = True

        return fish_count

    # Function to find the maximum number of fishes
    def findMaxFish(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        result = 0
        visited = [[False] * num_cols for _ in range(num_rows)]

        # Iterating through the entire grid
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] and not visited[i][j]:
                    result = max(result, self.count_fishes(grid, visited, i, j))

        return result


class SolutionUnionFind:
    def findMaxFish(self, grid):
        def find_parent(cell_index):  # Find the root of a component
            if parent[cell_index] != cell_index:
                parent[cell_index] = find_parent(parent[cell_index])  # Path compression
            return parent[cell_index]

        def union_components(cell_index1, cell_index2):  # Union two components
            root1 = find_parent(cell_index1)
            root2 = find_parent(cell_index2)
            if root1 != root2:
                # Union by size to optimize tree height
                if component_size[root1] < component_size[root2]:
                    root1, root2 = root2, root1
                parent[root2] = root1
                component_size[root1] += component_size[root2]
                total_fish[root1] += total_fish[root2]

        row_count, column_count = len(grid), len(grid[0])
        total_cells = row_count * column_count

        # Initialize Union-Find structures
        parent = list(range(total_cells))
        component_size = [1] * total_cells
        total_fish = [0] * total_cells

        # Set initial fish count for each cell
        for row in range(row_count):
            for column in range(column_count):
                cell_index = row * column_count + column
                total_fish[cell_index] = grid[row][column]

        # Direction vectors for neighbors (right, left, down, up)
        delta_row = [0, 0, 1, -1]
        delta_column = [1, -1, 0, 0]

        # Merge connected components
        for row in range(row_count):
            for column in range(column_count):
                if grid[row][column] > 0:  # Process only water cells with fish
                    cell_index = row * column_count + column
                    for direction in range(4):
                        neighbor_row = row + delta_row[direction]
                        neighbor_column = column + delta_column[direction]
                        if (
                            0 <= neighbor_row < row_count
                            and 0 <= neighbor_column < column_count
                            and grid[neighbor_row][neighbor_column] > 0
                        ):
                            neighbor_index = (
                                neighbor_row * column_count + neighbor_column
                            )
                            union_components(cell_index, neighbor_index)

        # Find the maximum fish in any component
        max_fish = 0
        for cell_index in range(total_cells):
            if find_parent(cell_index) == cell_index:  # Check if `cell_index` is a root
                max_fish = max(max_fish, total_fish[cell_index])

        return max_fish
