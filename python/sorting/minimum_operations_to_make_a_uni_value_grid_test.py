import unittest

from .minimum_operations_to_make_a_uni_value_grid import Solution


class TestMinOperations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sample_case(self):
        grid = [[2, 4], [6, 8]]
        x = 2
        result = self.solution.minOperations(grid, x)
        self.assertEqual(result, 4)

    def test_sample_case_2(self):
        grid = [[1, 5], [2, 3]]
        x = 1
        result = self.solution.minOperations(grid, x)
        self.assertEqual(result, 5)

    def test_sample_case_3(self):
        grid = [[1, 2], [3, 4]]
        x = 2
        result = self.solution.minOperations(grid, x)
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
