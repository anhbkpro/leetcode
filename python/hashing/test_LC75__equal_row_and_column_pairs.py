import unittest

from .LC75__equal_row_and_column_pairs import Solution


class TestEqualPairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_grid(self):
        self.assertEqual(self.solution.equalPairs([]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.equalPairs([[1]]), 1)

    def test_2x2_grid(self):
        # Test case with 2x2 grid
        grid = [[1, 2], [2, 1]]
        self.assertEqual(self.solution.equalPairs(grid), 2)

        # Test case with no equal pairs
        grid = [[1, 2], [3, 4]]
        self.assertEqual(self.solution.equalPairs(grid), 0)

    def test_3x3_grid(self):
        # Test case with 3x3 grid and multiple equal pairs
        grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
        self.assertEqual(self.solution.equalPairs(grid), 1)

        # Test case with all rows and columns equal
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(self.solution.equalPairs(grid), 9)

    def test_complex_cases(self):
        # Test case with larger grid and complex patterns
        grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
        self.assertEqual(self.solution.equalPairs(grid), 3)

        # Test case with no equal pairs
        grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.assertEqual(self.solution.equalPairs(grid), 0)

    def test_edge_cases(self):
        # Test case with negative numbers
        grid = [[-1, -2], [-2, -1]]
        self.assertEqual(self.solution.equalPairs(grid), 2)

        # Test case with zero
        grid = [[0, 0], [0, 0]]
        self.assertEqual(self.solution.equalPairs(grid), 4)

        # Test case with large numbers
        grid = [[1000, 2000], [2000, 1000]]
        self.assertEqual(self.solution.equalPairs(grid), 2)

    def test_symmetric_grids(self):
        # Test case with symmetric grid
        grid = [[1, 2, 3], [2, 1, 2], [3, 2, 1]]
        self.assertEqual(self.solution.equalPairs(grid), 3)

        # Test case with anti-symmetric grid
        grid = [[1, -2, 3], [2, 1, -2], [-3, 2, 1]]
        self.assertEqual(self.solution.equalPairs(grid), 0)

    def test_repeated_values(self):
        # Test case with repeated values in rows and columns
        grid = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        self.assertEqual(self.solution.equalPairs(grid), 0)

        # Test case with some repeated values
        grid = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]
        self.assertEqual(self.solution.equalPairs(grid), 5)


if __name__ == "__main__":
    unittest.main()
