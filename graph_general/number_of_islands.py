from typing import List


class SolutionDFS:
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def _check_in_bound(self, grid: List[List[str]], row: int, col: int) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def _dfs(self, grid: List[List[str]], row: int, col: int, visited):
        if (
            (row, col) in visited
            or not self._check_in_bound(grid, row, col)
            or grid[row][col] != "1"
        ):
            return

        visited.add((row, col))
        for x, y in self.dirs:
            next_row, next_col = row + x, col + y
            self._dfs(grid, next_row, next_col, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    num_islands += 1
                    self._dfs(grid, row, col, visited)

        return num_islands


class SolutionBFS:
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def _check_in_bound(self, grid: List[List[str]], row: int, col: int) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    num_islands += 1
                    q = [(row, col)]
                    while q:
                        r, c = q.pop()
                        visited.add((r, c))
                        for x, y in self.dirs:
                            next_row, next_col = r + x, c + y
                            if (
                                self._check_in_bound(grid, next_row, next_col)
                                and (next_row, next_col) not in visited
                                and grid[next_row][next_col] == "1"
                            ):
                                q.append((next_row, next_col))
                                visited.add((next_row, next_col))

        return num_islands


class UnionFind:
    def __init__(self, grid):
        self.count = 0
        m, n = len(grid), len(grid[0])
        self.parent = []
        self.rank = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i * n + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class SolutionUnionFind:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        uf = UnionFind(grid)

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    if r - 1 >= 0 and grid[r - 1][c] == "1":
                        uf.union(r * nc + c, (r - 1) * nc + c)
                    if r + 1 < nr and grid[r + 1][c] == "1":
                        uf.union(r * nc + c, (r + 1) * nc + c)
                    if c - 1 >= 0 and grid[r][c - 1] == "1":
                        uf.union(r * nc + c, r * nc + c - 1)
                    if c + 1 < nc and grid[r][c + 1] == "1":
                        uf.union(r * nc + c, r * nc + c + 1)

        return uf.getCount()