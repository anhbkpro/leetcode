import unittest

from .LC75__number_of_provinces import Solution


class TestNumberOfProvinces(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        expected = 2
        self.assertEqual(self.solution.findCircleNum(isConnected), expected)

    def test_single_city(self):
        isConnected = [[1]]
        expected = 1
        self.assertEqual(self.solution.findCircleNum(isConnected), expected)

    def test_all_connected(self):
        isConnected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected = 1
        self.assertEqual(self.solution.findCircleNum(isConnected), expected)

    def test_none_connected(self):
        isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        expected = 3
        self.assertEqual(self.solution.findCircleNum(isConnected), expected)

    def test_leetcode_example(self):
        isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        expected = 2
        self.assertEqual(self.solution.findCircleNum(isConnected), expected)

    def test_four_cities(self):
        isConnected = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
        expected = 1
        self.assertEqual(self.solution.findCircleNum(isConnected), expected)

    def test_five_cities(self):
        isConnected = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
        ]
        expected = 3
        self.assertEqual(self.solution.findCircleNum(isConnected), expected)

    def test_empty_matrix(self):
        isConnected = []
        expected = 0
        self.assertEqual(self.solution.findCircleNum(isConnected), expected)

    def test_large_matrix(self):
        # Test with 100 cities (all connected)
        isConnected = [[1] * 100 for _ in range(100)]
        expected = 1
        self.assertEqual(self.solution.findCircleNum(isConnected), expected)

    def test_disconnected_groups(self):
        isConnected = [
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1],
        ]
        expected = 3
        self.assertEqual(self.solution.findCircleNum(isConnected), expected)

    def test_chain_connection(self):
        isConnected = [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]]
        expected = 1
        self.assertEqual(self.solution.findCircleNum(isConnected), expected)

    def test_invalid_matrix(self):
        isConnected = [[1, 0], [0, 1], [1, 1]]  # Non-square matrix
        with self.assertRaises(IndexError):
            self.solution.findCircleNum(isConnected)


if __name__ == "__main__":
    unittest.main()
