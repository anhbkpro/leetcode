from .number_of_islands import SolutionDFS, SolutionBFS, SolutionUnionFind
import pytest


@pytest.fixture(params=[SolutionDFS, SolutionBFS, SolutionUnionFind])
def solution(request):
    return request.param()


def test_single_island(solution):
    grid = [["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]]
    assert solution.numIslands(grid) == 1


def test_no_islands(solution):
    grid = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
    assert solution.numIslands(grid) == 0


def test_multiple_islands(solution):
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert solution.numIslands(grid) == 3


def test_diagonal_islands(solution):
    grid = [["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]]
    assert solution.numIslands(grid) == 5


def test_single_cell_islands(solution):
    grid = [["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]]
    assert solution.numIslands(grid) == 5


def test_empty_grid(solution):
    grid = []
    assert solution.numIslands(grid) == 0


def test_single_row(solution):
    grid = [["1", "0", "1", "1", "0", "1", "1"]]
    assert solution.numIslands(grid) == 3


def test_single_column(solution):
    grid = [["1"], ["0"], ["1"], ["1"]]
    assert solution.numIslands(grid) == 2


def test_complex_island_shape(solution):
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "0", "0", "0", "0"],
        ["1", "1", "0", "1", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert solution.numIslands(grid) == 2


def test_boundary_islands(solution):
    grid = [
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1"],
    ]
    assert solution.numIslands(grid) == 1


def test_alternating_pattern(solution):
    grid = [["1", "0", "1", "0"], ["0", "1", "0", "1"], ["1", "0", "1", "0"]]
    assert solution.numIslands(grid) == 6
