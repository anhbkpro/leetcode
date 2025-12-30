import unittest
from .grid_game import Solution


class TestGridGame(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        grid = [[2, 5, 4], [1, 5, 1]]
        expected = 4
        result = self.solution.gridGame(grid)
        self.assertEqual(result, expected)

    def test_single_column(self):
        grid = [[5], [2]]
        expected = 0
        result = self.solution.gridGame(grid)
        self.assertEqual(result, expected)

    def test_all_zeros(self):
        grid = [[0, 0, 0], [0, 0, 0]]
        expected = 0
        result = self.solution.gridGame(grid)
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        grid = [[1000000, 1000000], [1000000, 1000000]]
        expected = 1000000
        result = self.solution.gridGame(grid)
        self.assertEqual(result, expected)

    def test_asymmetric_grid(self):
        grid = [[1, 3, 1, 15], [1, 3, 3, 1]]
        expected = 7
        result = self.solution.gridGame(grid)
        self.assertEqual(result, expected)

    def test_equal_paths(self):
        grid = [[3, 3, 3], [3, 3, 3]]
        expected = 3
        result = self.solution.gridGame(grid)
        self.assertEqual(result, expected)

    def test_large_grid(self):
        grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
        expected = 40
        result = self.solution.gridGame(grid)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
