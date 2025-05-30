import unittest
from find_closest_node_to_given_two_nodes import Solution


class TestFindClosestNodeToGivenTwoNodes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_path(self):
        edges = [2, 2, 3, -1]
        node1 = 0
        node2 = 1
        self.assertEqual(self.solution.closestMeetingNode(edges, node1, node2), 2)

    def test_disconnected_nodes(self):
        edges = [1, -1, -1, -1]
        node1 = 0
        node2 = 2
        self.assertEqual(self.solution.closestMeetingNode(edges, node1, node2), -1)

    def test_cycle(self):
        edges = [1, 2, 0, -1]
        node1 = 0
        node2 = 2
        self.assertEqual(self.solution.closestMeetingNode(edges, node1, node2), 0)

    def test_same_starting_node(self):
        edges = [1, 2, 3, -1]
        node1 = 0
        node2 = 0
        self.assertEqual(self.solution.closestMeetingNode(edges, node1, node2), 0)

    def test_no_path(self):
        edges = [-1, -1, -1, -1]
        node1 = 0
        node2 = 1
        self.assertEqual(self.solution.closestMeetingNode(edges, node1, node2), -1)

    def test_larger_graph(self):
        edges = [4, 4, 8, -1, 9, 6, 9, 7, 1, 0]
        node1 = 5
        node2 = 6
        self.assertEqual(self.solution.closestMeetingNode(edges, node1, node2), 6)

    def test_multiple_paths(self):
        edges = [1, 2, 3, 4, 5, -1]
        node1 = 0
        node2 = 4
        self.assertEqual(self.solution.closestMeetingNode(edges, node1, node2), 4)

    def test_self_loop(self):
        edges = [0, 2, 3, -1]
        node1 = 0
        node2 = 1
        self.assertEqual(self.solution.closestMeetingNode(edges, node1, node2), -1)


if __name__ == "__main__":
    unittest.main()
