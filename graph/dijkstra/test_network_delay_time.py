import unittest
from .network_delay_time import BFSSolution, DijkstraSolution


class BaseTestNetworkDelayTime:
    """Base test class containing all test cases."""

    def test_simple_path(self):
        # Test case with a simple linear path
        times = [[1, 2, 1], [2, 3, 2]]  # 1->2->3
        n = 3
        k = 1  # Starting node
        expected = 3  # Total time: 1 + 2 = 3
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, expected)

    def test_multiple_paths(self):
        # Test case with multiple paths to nodes
        times = [
            [1, 2, 1],  # Path 1: 1->2
            [2, 3, 2],  # Path 1: 2->3 (total: 3)
            [1, 3, 5],  # Path 2: 1->3 (total: 5)
        ]
        n = 3
        k = 1
        expected = 3  # Shorter path through node 2
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, expected)

    def test_unreachable_node(self):
        # Test case where one node is unreachable
        times = [[1, 2, 1]]  # No path to node 3
        n = 3
        k = 1
        expected = -1  # Node 3 is unreachable
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, expected)

    def test_start_node_isolated(self):
        # Test case where start node has no outgoing edges
        times = [[2, 3, 1]]  # Start node 1 has no edges
        n = 3
        k = 1
        expected = -1  # Other nodes unreachable from start
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, expected)

    def test_cycle_in_graph(self):
        # Test case with a cycle in the graph
        times = [[1, 2, 1], [2, 3, 1], [3, 1, 1]]  # Creates cycle 1->2->3->1
        n = 3
        k = 1
        expected = 2  # Time to reach furthest node (node 3)
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, expected)

    def test_multiple_signals_same_node(self):
        # Test case where a node receives multiple signals
        times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]  # Direct path to 3 (slower)
        n = 3
        k = 1
        expected = 3  # Should take shorter path through node 2
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, expected)

    def test_single_node(self):
        # Test case with only one node
        times = []
        n = 1
        k = 1
        expected = 0  # No time needed for single node
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, expected)

    def test_large_weights(self):
        # Test case with large travel times
        times = [[1, 2, 1000000], [2, 3, 1000000]]
        n = 3
        k = 1
        expected = 2000000  # Sum of large weights
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, expected)

    def test_complex_network(self):
        # Test case with a more complex network topology
        times = [
            [1, 2, 1],
            [1, 3, 3],  # Direct paths from 1
            [2, 3, 1],
            [2, 4, 4],  # Paths from 2
            [3, 4, 1],  # Path from 3 to 4
        ]
        n = 4
        k = 1
        expected = 3  # Time for signal to reach all nodes
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, expected)


class TestBFS(unittest.TestCase, BaseTestNetworkDelayTime):
    def setUp(self):
        self.solution = BFSSolution()


class TestDijkstra(unittest.TestCase, BaseTestNetworkDelayTime):
    def setUp(self):
        self.solution = DijkstraSolution()


if __name__ == "__main__":
    unittest.main()
