import unittest
from .making_a_large_island import Solution


class TestLargestIsland(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_grid(self):
        grid = [[0]]
        self.assertEqual(self.solution.largestIsland(grid), 1)

    def test_full_grid(self):
        grid = [[1, 1], [1, 1]]
        self.assertEqual(self.solution.largestIsland(grid), 4)

    def test_single_island(self):
        grid = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
        self.assertEqual(self.solution.largestIsland(grid), 5)

    def test_multiple_islands(self):
        grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        self.assertEqual(self.solution.largestIsland(grid), 3)

    def test_no_possible_expansion(self):
        grid = [[1, 1], [1, 0]]
        self.assertEqual(self.solution.largestIsland(grid), 4)

    def test_complex_case(self):
        grid = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
        self.assertEqual(self.solution.largestIsland(grid), 9)

    def test_all_zeros(self):
        grid = [[0, 0], [0, 0]]
        self.assertEqual(self.solution.largestIsland(grid), 1)


if __name__ == "__main__":
    unittest.main()
