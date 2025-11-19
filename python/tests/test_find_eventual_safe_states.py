import unittest
from toposort.find_eventual_safe_states import SolutionTopo


class TestFindEventualSafeStates(unittest.TestCase):
    def setUp(self):
        self.solution = SolutionTopo()

    def test_example_1(self):
        # Test case from LeetCode example
        graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
        expected = [2, 4, 5, 6]
        self.assertEqual(self.solution.eventualSafeNodes(graph), expected)

    def test_example_2(self):
        # Another test case from LeetCode
        graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
        expected = [4]
        self.assertEqual(self.solution.eventualSafeNodes(graph), expected)

    def test_empty_graph(self):
        # Test with empty graph
        graph = []
        expected = []
        self.assertEqual(self.solution.eventualSafeNodes(graph), expected)

    def test_single_node(self):
        # Test with a single node with no edges
        graph = [[]]
        expected = [0]  # Node 0 is safe as it has no outgoing edges
        self.assertEqual(self.solution.eventualSafeNodes(graph), expected)

    def test_all_nodes_terminal(self):
        # Test when all nodes are terminal (no outgoing edges)
        graph = [[], [], [], []]
        expected = [0, 1, 2, 3]  # All nodes are safe
        self.assertEqual(self.solution.eventualSafeNodes(graph), expected)

    def test_cycle(self):
        # Test with a cycle in the graph
        graph = [[1], [2], [1]]  # Cycle: 0->1->2->1
        expected = []  # No safe nodes due to cycle
        self.assertEqual(self.solution.eventualSafeNodes(graph), expected)

    def test_self_loop(self):
        # Test with a self-loop
        graph = [[0]]  # Node points to itself
        expected = []  # No safe nodes due to self-loop
        self.assertEqual(self.solution.eventualSafeNodes(graph), expected)

    def test_complex_graph(self):
        # Test with a more complex graph structure
        graph = [
            [1, 2],  # 0 -> 1,2
            [2, 3],  # 1 -> 2,3
            [3],  # 2 -> 3
            [4, 5],  # 3 -> 4,5
            [],  # 4 (terminal)
            [],  # 5 (terminal)
        ]
        expected = [0, 1, 2, 3, 4, 5]  # All nodes that eventually lead to 4 or 5
        self.assertEqual(self.solution.eventualSafeNodes(graph), expected)


if __name__ == "__main__":
    unittest.main()
