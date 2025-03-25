import unittest
from .check_if_grid_can_be_cut_into_sections import Solution


class TestCheckValidCuts(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_rectangles(self):
        # Test case with no rectangles
        n = 0
        rectangles = []
        result = self.solution.checkValidCuts(n, rectangles)
        self.assertFalse(result)

    def test_single_rectangle(self):
        # Test case with a single rectangle
        n = 1
        rectangles = [[1, 1, 2, 2]]
        result = self.solution.checkValidCuts(n, rectangles)
        self.assertFalse(result)

    def test_two_rectangles(self):
        # Test case with two rectangles
        n = 2
        rectangles = [[1, 1, 2, 2], [3, 1, 4, 2]]
        result = self.solution.checkValidCuts(n, rectangles)
        self.assertFalse(result)

    def test_three_rectangles_horizontal_cut(self):
        # Test case with three rectangles that can be cut horizontally
        n = 3
        rectangles = [
            [1, 1, 2, 2],  # Bottom rectangle
            [1, 3, 2, 4],  # Middle rectangle
            [1, 5, 2, 6],  # Top rectangle
        ]
        result = self.solution.checkValidCuts(n, rectangles)
        self.assertTrue(result)

    def test_three_rectangles_vertical_cut(self):
        # Test case with three rectangles that can be cut vertically
        n = 3
        rectangles = [
            [1, 1, 2, 2],  # Left rectangle
            [3, 1, 4, 2],  # Middle rectangle
            [5, 1, 6, 2],  # Right rectangle
        ]
        result = self.solution.checkValidCuts(n, rectangles)
        self.assertTrue(result)

    def test_overlapping_rectangles(self):
        # Test case with overlapping rectangles
        n = 3
        rectangles = [
            [1, 1, 3, 3],  # Large rectangle
            [2, 2, 4, 4],  # Overlapping rectangle
            [3, 3, 5, 5],  # Another overlapping rectangle
        ]
        result = self.solution.checkValidCuts(n, rectangles)
        self.assertFalse(result)

    def test_adjacent_rectangles(self):
        # Test case with adjacent rectangles
        n = 3
        rectangles = [
            [1, 1, 2, 2],  # First rectangle
            [2, 1, 3, 2],  # Adjacent to first
            [3, 1, 4, 2],  # Adjacent to second
        ]
        result = self.solution.checkValidCuts(n, rectangles)
        self.assertTrue(result)

    def test_merge_intervals(self):
        # Test the merge_intervals helper method
        intervals = [[1, 3], [2, 4], [5, 7]]
        expected = [[1, 4], [5, 7]]
        result = self.solution.merge_intervals(intervals)
        self.assertEqual(result, expected)

    def test_extract_dimension_intervals(self):
        # Test the extract_dimension_intervals helper method
        rectangles = [[1, 2, 3, 4], [5, 6, 7, 8]]

        # Test horizontal intervals
        horizontal = self.solution.extract_dimension_intervals(
            rectangles, horizontal=True
        )
        self.assertEqual(horizontal, [[1, 3], [5, 7]])

        # Test vertical intervals
        vertical = self.solution.extract_dimension_intervals(
            rectangles, horizontal=False
        )
        self.assertEqual(vertical, [[2, 4], [6, 8]])

    def test_has_valid_cuts(self):
        # Test the has_valid_cuts helper method
        # Test with valid cuts
        valid_intervals = [[1, 2], [3, 4], [5, 6]]
        self.assertTrue(self.solution.has_valid_cuts(valid_intervals))

        # Test with invalid cuts (merged into less than 3 intervals)
        invalid_intervals = [[1, 3], [2, 4], [3, 5]]
        self.assertFalse(self.solution.has_valid_cuts(invalid_intervals))


if __name__ == "__main__":
    unittest.main()
