import unittest
from .maximum_number_of_fish_in_a_grid import (
    SolutionDFS,
    SolutionBFS,
    SolutionUnionFind,
)


class TestMaximumNumberOfFishInAGrid(unittest.TestCase):
    def setUp(self):
        self.solutions = [SolutionDFS(), SolutionBFS(), SolutionUnionFind()]

    def test_example_1(self):
        grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
        expected = 7
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__):
                self.assertEqual(solution.findMaxFish(grid), expected)

    def test_example_2(self):
        grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
        expected = 1
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__):
                self.assertEqual(solution.findMaxFish(grid), expected)

    def test_no_fish(self):
        grid = [[0, 0], [0, 0]]
        expected = 0
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__):
                self.assertEqual(solution.findMaxFish(grid), expected)

    def test_all_fish(self):
        grid = [[1, 2], [3, 4]]
        expected = 10
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__):
                self.assertEqual(solution.findMaxFish(grid), expected)

    def test_single_cell(self):
        grid = [[5]]
        expected = 5
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__):
                self.assertEqual(solution.findMaxFish(grid), expected)


if __name__ == "__main__":
    unittest.main()
