import unittest

from heaps.ipo import Solution


class TestIPO(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Test case from LeetCode example 1
        k = 2
        w = 0
        profits = [1, 2, 3]
        capital = [0, 1, 1]
        result = self.solution.findMaximizedCapital(k, w, profits, capital)
        self.assertEqual(result, 4)  # Can first take project 0, then project 2

    def test_example_2(self):
        # Test case from LeetCode example 2
        k = 3
        w = 0
        profits = [1, 2, 3]
        capital = [0, 1, 2]
        result = self.solution.findMaximizedCapital(k, w, profits, capital)
        self.assertEqual(result, 6)  # Can take all projects in order

    def test_no_available_projects(self):
        # Test when initial capital is too low for any project
        k = 1
        w = 0
        profits = [1, 2, 3]
        capital = [1, 2, 3]
        result = self.solution.findMaximizedCapital(k, w, profits, capital)
        self.assertEqual(result, 0)

    def test_single_project(self):
        # Test with just one project
        k = 1
        w = 1
        profits = [2]
        capital = [1]
        result = self.solution.findMaximizedCapital(k, w, profits, capital)
        self.assertEqual(result, 3)

    def test_k_greater_than_available_projects(self):
        # Test when k is larger than number of available projects
        k = 5
        w = 1
        profits = [1, 2]
        capital = [0, 0]
        result = self.solution.findMaximizedCapital(k, w, profits, capital)
        self.assertEqual(result, 4)  # Can only take 2 projects despite k=5


if __name__ == "__main__":
    unittest.main()
