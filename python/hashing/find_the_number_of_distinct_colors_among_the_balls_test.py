import unittest

from .find_the_number_of_distinct_colors_among_the_balls import Solution


class TestFindDistinctColors(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        limit = 4
        queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
        expected = [1, 2, 2, 3]
        result = self.solution.distinctColors(limit, queries)
        self.assertEqual(result, expected)

    def test_example_2(self):
        limit = 4
        queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
        expected = [1, 2, 2, 3, 4]
        result = self.solution.distinctColors(limit, queries)
        self.assertEqual(result, expected)

    def test_empty_queries(self):
        limit = 4
        queries = []
        expected = []
        result = self.solution.distinctColors(limit, queries)
        self.assertEqual(result, expected)

    def test_single_query(self):
        limit = 1
        queries = [[0, 1]]
        expected = [1]
        result = self.solution.distinctColors(limit, queries)
        self.assertEqual(result, expected)

    def test_same_color_different_balls(self):
        limit = 3
        queries = [[0, 1], [1, 1], [2, 1]]
        expected = [1, 1, 1]
        result = self.solution.distinctColors(limit, queries)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
