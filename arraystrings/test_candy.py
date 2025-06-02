import unittest
from candy import Solution


class TestCandy(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        self.assertEqual(self.solution.candy([]), 0)

    def test_single_child(self):
        self.assertEqual(self.solution.candy([1]), 1)
        self.assertEqual(self.solution.candy([5]), 1)

    def test_two_children(self):
        self.assertEqual(self.solution.candy([1, 2]), 3)  # [1, 2]
        self.assertEqual(self.solution.candy([2, 1]), 3)  # [2, 1]
        self.assertEqual(self.solution.candy([1, 1]), 2)  # [1, 1]

    def test_increasing_sequence(self):
        self.assertEqual(self.solution.candy([1, 2, 3]), 6)  # [1, 2, 3]
        self.assertEqual(self.solution.candy([1, 2, 3, 4]), 10)  # [1, 2, 3, 4]

    def test_decreasing_sequence(self):
        self.assertEqual(self.solution.candy([3, 2, 1]), 6)  # [3, 2, 1]
        self.assertEqual(self.solution.candy([4, 3, 2, 1]), 10)  # [4, 3, 2, 1]

    def test_equal_ratings(self):
        self.assertEqual(self.solution.candy([1, 1, 1]), 3)  # [1, 1, 1]
        self.assertEqual(self.solution.candy([2, 2, 2, 2]), 4)  # [1, 1, 1, 1]

    def test_mixed_ratings(self):
        self.assertEqual(self.solution.candy([1, 0, 2]), 5)  # [2, 1, 2]
        self.assertEqual(self.solution.candy([1, 2, 2]), 4)  # [1, 2, 1]
        self.assertEqual(self.solution.candy([1, 3, 2, 2, 1]), 7)  # [1, 2, 1, 2, 1]

    def test_complex_cases(self):
        self.assertEqual(self.solution.candy([1, 2, 3, 1, 0]), 9)  # [1, 2, 3, 2, 1]
        self.assertEqual(
            self.solution.candy([1, 2, 3, 3, 2, 1]), 12
        )  # [1, 2, 3, 3, 2, 1]
        self.assertEqual(
            self.solution.candy([1, 2, 3, 4, 3, 2, 1]), 16
        )  # [1, 2, 3, 4, 3, 2, 1]

    def test_edge_cases(self):
        self.assertEqual(self.solution.candy([1, 1, 1, 1]), 4)  # [1, 1, 1, 1]
        self.assertEqual(self.solution.candy([1, 2, 1, 2, 1]), 7)  # [1, 2, 1, 2, 1]
        self.assertEqual(
            self.solution.candy([1, 2, 3, 4, 5, 4, 3, 2, 1]), 25
        )  # [1, 2, 3, 4, 5, 4, 3, 2, 1]


if __name__ == "__main__":
    unittest.main()
