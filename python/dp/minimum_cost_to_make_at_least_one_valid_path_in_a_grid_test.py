import pytest

from .minimum_cost_to_make_at_least_one_valid_path_in_a_grid import Solution


def test_2x2_grid_no_changes_needed():
    solution = Solution()
    grid = [[1, 1], [3, 1]]
    assert solution.minCost(grid) == 1


def test_2x2_grid_one_change_needed():
    solution = Solution()
    grid = [[1, 2], [3, 1]]
    assert solution.minCost(grid) == 1


def test_3x3_grid_multiple_paths():
    solution = Solution()
    grid = [[1, 1, 1], [4, 3, 1], [4, 2, 2]]
    assert solution.minCost(grid) == 2


def test_3x3_grid_optimal_path():
    solution = Solution()
    grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert solution.minCost(grid) == 2


def test_1x3_horizontal_grid():
    solution = Solution()
    grid = [[1, 1, 1]]
    assert solution.minCost(grid) == 0


def test_3x1_vertical_grid():
    solution = Solution()
    grid = [[3], [3], [1]]
    assert solution.minCost(grid) == 0


def test_grid_all_wrong_directions():
    solution = Solution()
    grid = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    assert solution.minCost(grid) == 4  # Need to change direction in at least 4 cells


def test_grid_with_cycle():
    solution = Solution()
    grid = [[1, 2], [4, 3]]
    assert solution.minCost(grid) == 1


def test_larger_grid():
    solution = Solution()
    grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
    assert solution.minCost(grid) == 3


def test_grid_with_boundary_pointing_arrows():
    solution = Solution()
    grid = [[4, 1, 2], [3, 2, 1], [1, 2, 4]]
    assert solution.minCost(grid) == 2


def test_minimum_grid():
    solution = Solution()
    grid = [[1]]
    assert solution.minCost(grid) == 0


def test_snake_pattern():
    solution = Solution()
    grid = [[1, 1, 1], [2, 2, 3], [1, 1, 1]]
    assert solution.minCost(grid) == 1


# Edge cases
def test_grid_all_up():
    solution = Solution()
    grid = [[4, 4], [4, 4]]
    assert solution.minCost(grid) == 2


def test_grid_all_same_invalid():
    solution = Solution()
    grid = [[3, 3], [3, 3]]
    assert solution.minCost(grid) == 1


# Property-based test helper
def test_grid_properties():
    solution = Solution()
    grid = [[1, 1, 1], [3, 3, 3], [1, 1, 1]]
    result = solution.minCost(grid)

    # Test properties that should always be true
    assert result >= 0, "Cost should never be negative"
    assert result <= len(grid) * len(grid[0]), "Cost should not exceed grid size"


# Helper function to test invalid inputs
def test_invalid_inputs():
    solution = Solution()

    # Empty grid
    with pytest.raises(IndexError):
        solution.minCost([])

    # Grid with empty rows
    with pytest.raises(IndexError):
        solution.minCost([[]])

    # Grid with inconsistent row lengths
    with pytest.raises(IndexError):
        solution.minCost([[1, 1], [1]])


# Test for performance with larger grid
def test_performance_large_grid():
    solution = Solution()
    n = 20  # 20x20 grid
    grid = [[1] * n for _ in range(n)]
    result = solution.minCost(grid)
    assert result == 19


def test_docstring_example():
    solution = Solution()
    grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
    assert solution.minCost(grid) == 3


# Parametrized test for different grid sizes
@pytest.mark.parametrize(
    "grid,expected",
    [
        ([[1]], 0),
        ([[1, 1]], 0),
        ([[3], [3]], 0),
        ([[1, 2], [3, 4]], 1),
    ],
)
def test_parametrized_grids(grid, expected):
    solution = Solution()
    assert solution.minCost(grid) == expected


# Test helper to verify grid constraints
def test_grid_constraints():
    solution = Solution()
    grid = [[1, 2, 3], [2, 3, 4], [3, 4, 1]]
    result = solution.minCost(grid)

    # Verify constraints
    num_rows, num_cols = len(grid), len(grid[0])
    assert all(
        1 <= grid[i][j] <= 4 for i in range(num_rows) for j in range(num_cols)
    ), "Grid values must be between 1 and 4"
    assert result >= 0, "Cost must be non-negative"
    assert result <= num_rows * num_cols, "Cost cannot exceed grid size"
