import unittest
from graph.most_profitable_path_in_a_tree import Solution


class TestMostProfitablePathInATree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_path(self):
        """Test with a simple linear path
        0 -- 1 -- 2
        Bob starts at node 2
        Amount: [1, 2, 3]
        """
        edges = [[0, 1], [1, 2]]
        bob = 2
        amount = [1, 2, 3]
        self.assertEqual(self.solution.mostProfitablePath(edges, bob, amount), 2)

    def test_y_shaped_tree(self):
        """Test with a Y-shaped tree
        Bob starts at node 3
        Amount: [-2, 4, 2, -4]
        """
        edges = [[0, 1], [0, 2], [1, 3]]
        bob = 3
        amount = [-2, 4, 2, -4]
        self.assertEqual(self.solution.mostProfitablePath(edges, bob, amount), 0)

    def test_balanced_tree(self):
        """Test with a balanced tree
             0
           /   \
          1     2
         / \   / \
        3   4 5   6
        Bob starts at node 4
        Amount: [1, 2, 3, 4, 5, 6, 7]
        """
        edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
        bob = 4
        amount = [1, 2, 3, 4, 5, 6, 7]
        expected = 11
        self.assertEqual(self.solution.mostProfitablePath(edges, bob, amount), expected)

    def test_negative_amounts(self):
        """Test with negative amounts in the tree
             0
           /   \
          1     2
        Bob starts at node 2
        Amount: [-5, -3, -1]
        """
        edges = [[0, 1], [0, 2]]
        bob = 2
        amount = [-5, -3, -1]
        expected = -5  # Alice gets full amount at node 0
        self.assertEqual(self.solution.mostProfitablePath(edges, bob, amount), expected)

    def test_single_edge(self):
        """Test with a single edge
        0 -- 1
        Bob starts at node 1
        Amount: [5, 3]
        """
        edges = [[0, 1]]
        bob = 1
        amount = [5, 3]
        expected = 5  # Alice gets full amount at node 0
        self.assertEqual(self.solution.mostProfitablePath(edges, bob, amount), expected)


if __name__ == "__main__":
    unittest.main()
