from .magic_squares_in_grid import Solution


class TestMagicSquaresInGrid:
    def setup_method(self):
        self.solution = Solution()

    def test_single_magic_square(self):
        """Test grid with one magic square"""
        grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
        assert self.solution.numMagicSquaresInside(grid) == 1

    def test_no_magic_squares(self):
        """Test grid with no magic squares"""
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert self.solution.numMagicSquaresInside(grid) == 0

    def test_multiple_magic_squares(self):
        """Test grid with multiple magic squares"""
        grid = [
            [4, 3, 8, 4, 3, 8],
            [9, 5, 1, 9, 5, 1],
            [2, 7, 6, 2, 7, 6],
            [4, 3, 8, 4, 3, 8],
            [9, 5, 1, 9, 5, 1],
            [2, 7, 6, 2, 7, 6],
        ]
        assert self.solution.numMagicSquaresInside(grid) == 4

    def test_small_grid(self):
        """Test grid smaller than 3x3"""
        grid = [[1, 2], [3, 4]]
        assert self.solution.numMagicSquaresInside(grid) == 0

    def test_exact_3x3_magic_square(self):
        """Test exact 3x3 magic square"""
        grid = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
        assert self.solution.numMagicSquaresInside(grid) == 1

    def test_exact_3x3_non_magic_square(self):
        """Test exact 3x3 non-magic square"""
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert self.solution.numMagicSquaresInside(grid) == 0

    def test_duplicate_numbers(self):
        """Test 3x3 with duplicate numbers"""
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        assert self.solution.numMagicSquaresInside(grid) == 0

    def test_numbers_out_of_range(self):
        """Test with numbers outside 1-9 range"""
        grid = [[0, 3, 8], [9, 5, 1], [2, 7, 6]]
        assert self.solution.numMagicSquaresInside(grid) == 0

    def test_large_numbers(self):
        """Test with numbers larger than 9"""
        grid = [[4, 3, 8], [9, 5, 10], [2, 7, 6]]
        assert self.solution.numMagicSquaresInside(grid) == 0

    def test_another_valid_magic_square(self):
        """Test another valid magic square configuration"""
        grid = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        assert self.solution.numMagicSquaresInside(grid) == 1

    def test_4x4_grid_with_magic_square(self):
        """Test 4x4 grid where first 3x3 is magic"""
        grid = [[4, 3, 8, 1], [9, 5, 1, 2], [2, 7, 6, 3]]
        assert self.solution.numMagicSquaresInside(grid) == 1

    def test_4x4_grid_where_last_3x3_is_magic(self):
        """Test 4x4 grid where last 3x3 is magic"""
        grid = [[1, 4, 3, 8], [2, 9, 5, 1], [3, 2, 7, 6]]
        assert self.solution.numMagicSquaresInside(grid) == 1

    def test_4x4_grid_no_magic_square(self):
        """Test 4x4 grid with no magic squares"""
        grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3]]
        assert self.solution.numMagicSquaresInside(grid) == 0
