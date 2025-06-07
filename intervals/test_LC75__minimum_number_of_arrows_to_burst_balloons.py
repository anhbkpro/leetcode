import unittest
from .LC75__minimum_number_of_arrows_to_burst_balloons import (
    SolutionSortByStart,
    SolutionSortByEnd,
)


class TestMinimumNumberOfArrowsToBurstBalloons(unittest.TestCase):
    def setUp(self):
        self.solution = SolutionSortByStart()
        self.solution_end = SolutionSortByEnd()

    def test_basic_case(self):
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        expected = 2
        self.assertEqual(self.solution.findMinArrowShots(points), expected)
        self.assertEqual(self.solution_end.findMinArrowShots(points), expected)

    def test_overlapping_balloons(self):
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]
        expected = 2
        self.assertEqual(self.solution.findMinArrowShots(points), expected)
        self.assertEqual(self.solution_end.findMinArrowShots(points), expected)

    def test_fully_overlapping_balloons(self):
        points = [[1, 6], [2, 8], [7, 12], [10, 16]]
        expected = 2
        self.assertEqual(self.solution.findMinArrowShots(points), expected)
        self.assertEqual(self.solution_end.findMinArrowShots(points), expected)

    def test_minimum_length(self):
        points = [[1, 2]]
        expected = 1
        self.assertEqual(self.solution.findMinArrowShots(points), expected)
        self.assertEqual(self.solution_end.findMinArrowShots(points), expected)

    def test_non_overlapping_balloons(self):
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        expected = 4
        self.assertEqual(self.solution.findMinArrowShots(points), expected)
        self.assertEqual(self.solution_end.findMinArrowShots(points), expected)

    def test_leetcode_example(self):
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        expected = 4
        self.assertEqual(self.solution.findMinArrowShots(points), expected)
        self.assertEqual(self.solution_end.findMinArrowShots(points), expected)

    def test_negative_coordinates(self):
        points = [[-10, -5], [-8, -3], [-6, -1], [-4, 1]]
        expected = 2
        self.assertEqual(self.solution.findMinArrowShots(points), expected)
        self.assertEqual(self.solution_end.findMinArrowShots(points), expected)

    def test_mixed_coordinates(self):
        points = [[-10, 5], [-8, 3], [-6, 1], [-4, -1]]
        expected = 1
        self.assertEqual(self.solution.findMinArrowShots(points), expected)
        self.assertEqual(self.solution_end.findMinArrowShots(points), expected)

    def test_same_start_points(self):
        points = [[1, 6], [1, 8], [1, 10], [1, 12]]
        expected = 1
        self.assertEqual(self.solution.findMinArrowShots(points), expected)
        self.assertEqual(self.solution_end.findMinArrowShots(points), expected)

    def test_same_end_points(self):
        points = [[1, 6], [2, 6], [3, 6], [4, 6]]
        expected = 1
        self.assertEqual(self.solution.findMinArrowShots(points), expected)
        self.assertEqual(self.solution_end.findMinArrowShots(points), expected)

    def test_min_boundary_values(self):
        points = [[-(2**31), -(2**31) + 1], [-(2**31) + 1, -(2**31) + 2]]
        expected = 1
        self.assertEqual(self.solution.findMinArrowShots(points), expected)
        self.assertEqual(self.solution_end.findMinArrowShots(points), expected)

    def test_max_boundary_values(self):
        points = [[2**31 - 2, 2**31 - 1], [2**31 - 3, 2**31 - 2]]
        expected = 1
        self.assertEqual(self.solution.findMinArrowShots(points), expected)
        self.assertEqual(self.solution_end.findMinArrowShots(points), expected)

    def test_large_number_of_balloons(self):
        # Test with 1000 balloons (well within the 10^5 constraint)
        points = [[i, i + 1] for i in range(1000)]
        expected = 500  # Every other balloon can be shot together
        self.assertEqual(self.solution.findMinArrowShots(points), expected)
        self.assertEqual(self.solution_end.findMinArrowShots(points), expected)

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            self.solution.findMinArrowShots([[]])  # Invalid point format
        with self.assertRaises(IndexError):
            self.solution_end.findMinArrowShots([[]])  # Invalid point format


if __name__ == "__main__":
    unittest.main()
