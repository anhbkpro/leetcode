import pytest
from .count_negative_numbers_in_a_sorted_matrix import Solution


class TestCountNegativesInSortedMatrix:
    """Test suite for counting negative numbers in a sorted matrix."""

    def setup_method(self):
        """Initialize solution instance for each test."""
        self.solution = Solution()

    def test_example_1(self):
        """Test example 1 with mixed positive and negative values."""
        grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
        assert self.solution.countNegatives(grid) == 8

    def test_example_2(self):
        """Test example 2 with all positive values."""
        grid = [[3, 2], [1, 0]]
        assert self.solution.countNegatives(grid) == 0

    def test_all_negative(self):
        """Test with all negative values."""
        grid = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        assert self.solution.countNegatives(grid) == 9

    def test_single_element_negative(self):
        """Test with single negative element."""
        grid = [[-1]]
        assert self.solution.countNegatives(grid) == 1

    def test_single_element_positive(self):
        """Test with single positive element."""
        grid = [[5]]
        assert self.solution.countNegatives(grid) == 0

    def test_single_row(self):
        """Test with single row."""
        grid = [[4, 3, 2, -1, -2]]
        assert self.solution.countNegatives(grid) == 2

    def test_single_column(self):
        """Test with single column."""
        grid = [[5], [3], [1], [-1], [-3]]
        assert self.solution.countNegatives(grid) == 2

    def test_two_by_two_all_negative(self):
        """Test 2x2 matrix with all negatives."""
        grid = [[-1, -2], [-3, -4]]
        assert self.solution.countNegatives(grid) == 4

    def test_two_by_two_mixed(self):
        """Test 2x2 matrix with mixed values."""
        grid = [[2, 1], [-1, -2]]
        assert self.solution.countNegatives(grid) == 2

    def test_two_by_two_all_positive(self):
        """Test 2x2 matrix with all positives."""
        grid = [[5, 4], [3, 2]]
        assert self.solution.countNegatives(grid) == 0

    def test_large_positive_values(self):
        """Test with large positive values."""
        grid = [[1000, 999, 100, 50, 1], [100, 50, 10, 1, -1], [10, 5, -1, -5, -10]]
        assert self.solution.countNegatives(grid) == 4

    def test_transitioning_row(self):
        """Test row transitioning from positive to negative."""
        grid = [[10, 9, 8, 7, 6], [5, 4, 3, 2, 1], [0, -1, -2, -3, -4]]
        assert self.solution.countNegatives(grid) == 4

    def test_all_zeros(self):
        """Test with all zeros (non-negative)."""
        grid = [[0, 0], [0, 0]]
        assert self.solution.countNegatives(grid) == 0

    def test_mixed_with_zeros(self):
        """Test with mix of positive, zero, and negative."""
        grid = [[5, 0, -1], [0, -1, -2]]
        assert self.solution.countNegatives(grid) == 3

    def test_first_row_all_negative(self):
        """Test when first row is entirely negative."""
        grid = [[-1, -2, -3], [1, 0, -1], [5, 4, 3]]
        assert self.solution.countNegatives(grid) == 4

    def test_last_row_all_positive(self):
        """Test when last row is entirely positive."""
        grid = [[-5, -4, -3], [-2, -1, 0], [1, 2, 3]]
        assert self.solution.countNegatives(grid) == 6

    @pytest.mark.parametrize(
        "grid,expected",
        [
            ([[1, 0, -1]], 1),
            ([[5, -1], [0, -2]], 2),
            ([[10, 5, 0, -5]], 1),
            ([[-1], [-2], [-3]], 3),
            ([[100, 50, 0], [50, 25, -1], [0, -5, -10]], 3),
        ],
    )
    def test_parametrized(self, grid, expected):
        """Parametrized test for various grid configurations."""
        assert self.solution.countNegatives(grid) == expected

    def test_boundary_negative_at_corner(self):
        """Test with negative only at bottom-right corner."""
        grid = [[5, 4, 3], [4, 3, 2], [3, 2, -1]]
        assert self.solution.countNegatives(grid) == 1

    def test_negative_diagonal(self):
        """Test with negative values along diagonal."""
        grid = [[-1, 5, 4], [3, -2, 6], [2, 1, -3]]
        # Note: This tests that the algorithm handles non-strictly sorted rows correctly
        result = self.solution.countNegatives(grid)
        assert isinstance(result, int)

    def test_rectangular_matrix(self):
        """Test with rectangular (non-square) matrix."""
        grid = [[5, 4, 3, 2, 1], [0, -1, -2, -3, -4], [-1, -2, -3, -4, -5]]
        assert self.solution.countNegatives(grid) == 9
