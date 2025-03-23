import unittest
from .find_the_closest_marked_node import Solution


class TestMinimumDistance(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_path(self):
        # Test case with a simple path to a marked node
        n = 3
        edges = [[0, 1, 1], [1, 2, 1]]
        s = 0
        marked = [2]
        expected = 2  # Path: 0->1->2 with total distance 2
        result = self.solution.minimumDistance(n, edges, s, marked)
        self.assertEqual(result, expected)

    def test_multiple_marked_nodes(self):
        # Test case with multiple marked nodes, should return shortest distance
        n = 4
        edges = [
            [0, 1, 2],  # Path to first marked node (1)
            [0, 2, 3],  # Path to second marked node (2)
            [0, 3, 1],  # Path to third marked node (3)
        ]
        s = 0
        marked = [1, 2, 3]
        expected = 1  # Shortest path is to node 3 with distance 1
        result = self.solution.minimumDistance(n, edges, s, marked)
        self.assertEqual(result, expected)

    def test_no_path_to_marked(self):
        # Test case where there's no path to any marked node
        n = 4
        edges = [[0, 1, 1], [1, 2, 1]]  # No path to node 3
        s = 0
        marked = [3]
        expected = -1  # No path exists to marked node
        result = self.solution.minimumDistance(n, edges, s, marked)
        self.assertEqual(result, expected)

    def test_start_node_marked(self):
        # Test case where the start node is marked
        n = 3
        edges = [[0, 1, 1], [1, 2, 1]]
        s = 0
        marked = [0, 2]
        expected = 0  # Start node is marked, so distance is 0
        result = self.solution.minimumDistance(n, edges, s, marked)
        self.assertEqual(result, expected)

    def test_multiple_paths_to_marked(self):
        # Test case with multiple paths to marked nodes
        n = 5
        edges = [
            [0, 1, 1],
            [1, 4, 3],  # Path 1 to node 4: length 4
            [0, 2, 2],
            [2, 4, 1],  # Path 2 to node 4: length 3
            [0, 3, 5],  # Path to node 3: length 5
        ]
        s = 0
        marked = [3, 4]
        expected = 3  # Shortest path is to node 4 via 0->2->4
        result = self.solution.minimumDistance(n, edges, s, marked)
        self.assertEqual(result, expected)

    def test_cycle_in_graph(self):
        # Test case with cycles in the graph
        n = 4
        edges = [
            [0, 1, 1],
            [1, 2, 1],
            [2, 3, 1],
            [3, 1, 1],  # Creates a cycle 1->2->3->1
        ]
        s = 0
        marked = [3]
        expected = 3  # Shortest path is 0->1->2->3
        result = self.solution.minimumDistance(n, edges, s, marked)
        self.assertEqual(result, expected)

    def test_large_weights(self):
        # Test case with large edge weights
        n = 3
        edges = [[0, 1, 1000000], [1, 2, 1000000]]
        s = 0
        marked = [2]
        expected = 2000000  # Total distance is 2,000,000
        result = self.solution.minimumDistance(n, edges, s, marked)
        self.assertEqual(result, expected)

    def test_empty_marked_nodes(self):
        # Test case with no marked nodes
        n = 3
        edges = [[0, 1, 1], [1, 2, 1]]
        s = 0
        marked = []
        expected = -1  # No marked nodes to reach
        result = self.solution.minimumDistance(n, edges, s, marked)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
