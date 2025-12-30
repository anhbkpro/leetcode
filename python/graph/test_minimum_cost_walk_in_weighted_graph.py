import unittest

from .minimum_cost_walk_in_weighted_graph import Solution


class TestMinimumCost(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_component(self):
        # Test case where all nodes are in the same component
        n = 4
        edges = [[0, 1, 3], [1, 2, 7], [2, 3, 15]]
        queries = [[0, 3], [1, 2], [0, 1]]
        expected = [3, 3, 3]  # All paths use the same component with cost 3
        result = self.solution.minimumCost(n, edges, queries)
        self.assertEqual(result, expected)

    def test_multiple_components(self):
        # Test case with multiple disconnected components
        n = 5
        edges = [[0, 1, 7], [1, 2, 7], [3, 4, 15]]
        queries = [[0, 2], [0, 3], [3, 4]]
        expected = [7, -1, 15]  # -1 for nodes in different components
        result = self.solution.minimumCost(n, edges, queries)
        self.assertEqual(result, expected)

    def test_empty_graph(self):
        # Test case with no edges
        n = 3
        edges = []
        queries = [[0, 1], [1, 2], [0, 2]]
        expected = [-1, -1, -1]  # All nodes are in separate components
        result = self.solution.minimumCost(n, edges, queries)
        self.assertEqual(result, expected)

    def test_single_node(self):
        # Test case with a single node
        n = 1
        edges = []
        queries = [[0, 0]]
        expected = [-1]  # Single node has no edges
        result = self.solution.minimumCost(n, edges, queries)
        self.assertEqual(result, expected)

    def test_complex_weights(self):
        # Test case with complex binary weights
        n = 4
        edges = [[0, 1, 15], [1, 2, 7], [2, 3, 3]]
        queries = [[0, 3], [0, 2], [1, 3]]
        expected = [
            3,
            3,
            3,
        ]  # All nodes are in the same component, so they share the same minimum cost
        result = self.solution.minimumCost(n, edges, queries)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
