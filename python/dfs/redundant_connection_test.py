import unittest

from .redundant_connection import SolutionBFS, SolutionDFS, SolutionUnionFind


class TestRedundantConnection(unittest.TestCase):
    def setUp(self):
        self.solutions = [SolutionDFS(), SolutionBFS(), SolutionUnionFind()]

    def test_example_1(self):
        """Test case where the redundant edge creates a cycle in a simple graph"""
        edges = [[1, 2], [1, 3], [2, 3]]
        expected = [2, 3]
        for solution in self.solutions:
            self.assertEqual(solution.findRedundantConnection(edges), expected)

    def test_example_2(self):
        """Test case with a more complex graph structure"""
        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        expected = [1, 4]
        for solution in self.solutions:
            self.assertEqual(solution.findRedundantConnection(edges), expected)

    def test_triangle_with_branch(self):
        """Test case with a triangle and an additional branch"""
        edges = [[1, 2], [2, 3], [3, 1], [1, 4]]
        expected = [3, 1]
        for solution in self.solutions:
            self.assertEqual(solution.findRedundantConnection(edges), expected)

    def test_multiple_cycles(self):
        """Test case where there are multiple possible cycles"""
        edges = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5], [5, 6], [6, 1]]
        expected = [4, 1]  # The first edge that creates a cycle in the traversal order
        for solution in self.solutions:
            self.assertEqual(solution.findRedundantConnection(edges), expected)


if __name__ == "__main__":
    unittest.main()
