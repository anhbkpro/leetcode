import unittest

from .merge_intervals import Solution


class TestMergeIntervals(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test example case with overlapping intervals"""
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_example_2(self):
        """Test example case with completely overlapping intervals"""
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_empty_intervals(self):
        """Test with empty list of intervals"""
        intervals = []
        expected = []
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_single_interval(self):
        """Test with single interval"""
        intervals = [[1, 2]]
        expected = [[1, 2]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_no_overlap(self):
        """Test when no intervals overlap"""
        intervals = [[1, 2], [4, 5], [7, 8]]
        expected = [[1, 2], [4, 5], [7, 8]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_all_overlap(self):
        """Test when all intervals overlap"""
        intervals = [[1, 4], [2, 3], [3, 6], [5, 7]]
        expected = [[1, 7]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_nested_intervals(self):
        """Test with nested intervals"""
        intervals = [[1, 6], [2, 4], [3, 5]]
        expected = [[1, 6]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_unsorted_intervals(self):
        """Test with unsorted intervals"""
        intervals = [[3, 6], [1, 3], [8, 10], [2, 4]]
        expected = [[1, 6], [8, 10]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_adjacent_intervals(self):
        """Test with adjacent intervals that should merge"""
        intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]
        expected = [[1, 5]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_negative_numbers(self):
        """Test with negative numbers in intervals"""
        intervals = [[-4, -1], [-1, 2], [1, 4]]
        expected = [[-4, 4]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_large_numbers(self):
        """Test with large numbers in intervals"""
        intervals = [[1, 1000000], [2, 999999], [1000000, 1000001]]
        expected = [[1, 1000001]]
        self.assertEqual(self.solution.merge(intervals), expected)


if __name__ == "__main__":
    unittest.main()
