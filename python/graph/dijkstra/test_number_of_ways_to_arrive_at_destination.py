import unittest

from .number_of_ways_to_arrive_at_destination import Solution


class TestCountPaths(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_path(self):
        # Test case with a single path from source to destination
        n = 3
        roads = [[0, 1, 1], [1, 2, 1]]
        expected = 1  # Only one way to reach destination
        result = self.solution.countPaths(n, roads)
        self.assertEqual(result, expected)

    def test_multiple_paths_same_time(self):
        # Test case with multiple paths having the same total time
        n = 4
        roads = [
            [0, 1, 1],
            [1, 3, 1],  # Path 1: 0->1->3 (time=2)
            [0, 2, 1],
            [2, 3, 1],  # Path 2: 0->2->3 (time=2)
        ]
        expected = 2  # Two different paths with same total time
        result = self.solution.countPaths(n, roads)
        self.assertEqual(result, expected)

    def test_multiple_paths_different_times(self):
        # Test case with multiple paths having different times
        n = 4
        roads = [
            [0, 1, 1],
            [1, 3, 2],  # Path 1: 0->1->3 (time=3)
            [0, 2, 1],
            [2, 3, 1],  # Path 2: 0->2->3 (time=2)
        ]
        expected = 1  # Only one shortest path
        result = self.solution.countPaths(n, roads)
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        # Test case with large travel times to check modulo handling
        n = 3
        roads = [
            [0, 1, 1000000],
            [1, 2, 1000000],  # Path 1: 0->1->2
            [0, 2, 2000000],  # Path 2: 0->2
        ]
        expected = 2  # Two paths with same total time
        result = self.solution.countPaths(n, roads)
        self.assertEqual(result, expected)

    def test_complex_graph(self):
        # Test case with a more complex graph structure
        n = 5
        roads = [
            [0, 1, 1],
            [1, 2, 1],
            [2, 4, 1],  # Path 1: 0->1->2->4
            [0, 3, 2],
            [3, 4, 1],  # Path 2: 0->3->4
            [0, 2, 2],  # Path 3: 0->2->4
        ]
        expected = 3  # Three shortest paths with time=3
        result = self.solution.countPaths(n, roads)
        self.assertEqual(result, expected)

    def test_multiple_shortest_paths(self):
        # Test case with multiple shortest paths through different routes
        n = 4
        roads = [
            [0, 1, 1],
            [1, 3, 1],  # Path 1: 0->1->3
            [0, 2, 1],
            [2, 3, 1],  # Path 2: 0->2->3
        ]
        expected = 2  # Two independent shortest paths
        result = self.solution.countPaths(n, roads)
        self.assertEqual(result, expected)

    def test_minimum_graph(self):
        # Test case with minimum possible graph (2 nodes)
        n = 2
        roads = [[0, 1, 1]]
        expected = 1  # One direct path
        result = self.solution.countPaths(n, roads)
        self.assertEqual(result, expected)

    def test_modulo_overflow(self):
        # Test case to verify modulo arithmetic for large number of paths
        n = 4
        roads = [
            [0, 1, 1],
            [1, 3, 1],
            [0, 2, 1],
            [2, 3, 1],
            [1, 2, 0],  # Creates many paths through intermediate nodes
        ]
        result = self.solution.countPaths(n, roads)
        self.assertLess(result, 1_000_000_007)  # Result should be within modulo bounds


if __name__ == "__main__":
    unittest.main()
