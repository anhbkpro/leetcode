import unittest
from .minimum_number_of_arrows_to_burst_balloons import Solution


class TestMinArrows(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        expected = 2
        result = self.solution.findMinArrowShots(points)
        self.assertEqual(result, expected)

    def test_example_2(self):
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        expected = 4
        result = self.solution.findMinArrowShots(points)
        self.assertEqual(result, expected)

    def test_example_3(self):
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]
        expected = 2
        result = self.solution.findMinArrowShots(points)
        self.assertEqual(result, expected)

    def test_overlapping_balloons(self):
        points = [[1, 5], [2, 3], [2, 4], [3, 4]]
        expected = 1
        result = self.solution.findMinArrowShots(points)
        self.assertEqual(result, expected)

    def test_single_balloon(self):
        points = [[1, 2]]
        expected = 1
        result = self.solution.findMinArrowShots(points)
        self.assertEqual(result, expected)

    def test_empty_points(self):
        points = []
        expected = 0
        result = self.solution.findMinArrowShots(points)
        self.assertEqual(result, expected)

    def test_negative_coordinates(self):
        points = [[-3, 0], [-2, -1], [1, 2]]
        expected = 2
        result = self.solution.findMinArrowShots(points)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
