import unittest

from arraystrings.count_servers_that_communicate import Solution


class TestCountServers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Test case where 2 servers can communicate
        grid = [[1, 0], [1, 1]]
        self.assertEqual(self.solution.countServers(grid), 3)

    def test_example_2(self):
        # Test case where servers are isolated
        grid = [[1, 0], [0, 1]]
        self.assertEqual(self.solution.countServers(grid), 0)

    def test_example_3(self):
        # Test case with larger grid and multiple communicating servers
        grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        self.assertEqual(self.solution.countServers(grid), 4)

    def test_single_server(self):
        # Test case with only one server
        grid = [[1]]
        self.assertEqual(self.solution.countServers(grid), 0)

    def test_all_servers(self):
        # Test case where all cells are servers
        grid = [[1, 1], [1, 1]]
        self.assertEqual(self.solution.countServers(grid), 4)

    def test_single_row(self):
        # Test case with servers in a single row
        grid = [[1, 1, 1]]
        self.assertEqual(self.solution.countServers(grid), 3)

    def test_single_column(self):
        # Test case with servers in a single column
        grid = [[1], [1], [1]]
        self.assertEqual(self.solution.countServers(grid), 3)


if __name__ == "__main__":
    unittest.main()
