from .maximum_number_of_points_from_grid_queries import Solution


def test_max_points_example1():
    solution = Solution()
    grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
    queries = [5, 6, 2]
    assert solution.maxPoints(grid, queries) == [5, 8, 1]


def test_max_points_example2():
    solution = Solution()
    grid = [[5, 2, 1], [1, 1, 2]]
    queries = [3]
    assert solution.maxPoints(grid, queries) == [0]


def test_max_points_single_cell():
    solution = Solution()
    grid = [[1]]
    queries = [1, 2, 3]
    assert solution.maxPoints(grid, queries) == [0, 1, 1]


def test_max_points_same_values():
    solution = Solution()
    grid = [[1, 1], [1, 1]]
    queries = [1, 2, 3]
    assert solution.maxPoints(grid, queries) == [0, 4, 4]


def test_max_points_increasing_values():
    solution = Solution()
    grid = [[1, 2], [3, 4]]
    queries = [1, 2, 3, 4, 5]
    assert solution.maxPoints(grid, queries) == [0, 1, 2, 3, 4]


def test_max_points_decreasing_values():
    solution = Solution()
    grid = [[4, 3], [2, 1]]
    queries = [1, 2, 3, 4, 5]
    assert solution.maxPoints(grid, queries) == [0, 0, 0, 0, 4]


def test_max_points_empty_queries():
    solution = Solution()
    grid = [[1, 2], [3, 4]]
    queries = []
    assert solution.maxPoints(grid, queries) == []
