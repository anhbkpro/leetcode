import unittest

from matrix.find_the_minimum_area_to_cover_all_ones_i import Solution


class TestMinimumArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test Example 1: [[0,1,0],[1,0,1]] should return 6"""
        grid = [[0, 1, 0], [1, 0, 1]]
        expected = 6
        result = self.solution.minimumArea(grid)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """Test Example 2: [[1,0],[0,0]] should return 1"""
        grid = [[1, 0], [0, 0]]
        expected = 1
        result = self.solution.minimumArea(grid)
        self.assertEqual(result, expected)

    def test_single_one(self):
        """Test grid with single 1 should return 1"""
        grid = [[1]]
        expected = 1
        result = self.solution.minimumArea(grid)
        self.assertEqual(result, expected)

    def test_all_ones(self):
        """Test grid with all ones"""
        grid = [[1, 1], [1, 1]]
        expected = 4
        result = self.solution.minimumArea(grid)
        self.assertEqual(result, expected)

    def test_ones_in_corners(self):
        """Test ones in opposite corners"""
        grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
        expected = 9
        result = self.solution.minimumArea(grid)
        self.assertEqual(result, expected)

    def test_ones_in_single_row(self):
        """Test ones in a single row"""
        grid = [[0, 1, 1, 0]]
        expected = 2
        result = self.solution.minimumArea(grid)
        self.assertEqual(result, expected)

    def test_ones_in_single_column(self):
        """Test ones in a single column"""
        grid = [[0], [1], [1], [0]]
        expected = 2
        result = self.solution.minimumArea(grid)
        self.assertEqual(result, expected)

    def test_large_grid_with_scattered_ones(self):
        """Test larger grid with scattered ones"""
        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
        ]
        # minx=1, maxx=4, miny=0, maxy=4
        # area = (4-1+1) * (4-0+1) = 4 * 5 = 20
        expected = 20
        result = self.solution.minimumArea(grid)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
