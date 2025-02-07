import unittest
from .insert_interval import SolutionLinearSearch, SolutionBinarySearch


class TestInsertIntervalBase:
    """Base test class for insert interval implementations"""

    def setUp(self):
        self.solution = self.get_solution()

    def test_example_1(self):
        """Test example case with insertion in the middle"""
        intervals = [[1, 3], [6, 9]]
        new_interval = [2, 5]
        expected = [[1, 5], [6, 9]]
        result = self.solution.insert(intervals.copy(), new_interval.copy())
        self.assertEqual(result, expected)
        # Verify input is not modified for linear search
        if isinstance(self.solution, SolutionLinearSearch):
            self.assertEqual(intervals, [[1, 3], [6, 9]])

    def test_example_2(self):
        """Test example case with overlapping multiple intervals"""
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        new_interval = [4, 8]
        expected = [[1, 2], [3, 10], [12, 16]]
        self.assertEqual(
            self.solution.insert(intervals.copy(), new_interval.copy()),
            expected
        )

    def test_empty_intervals(self):
        """Test with empty list of intervals"""
        intervals = []
        new_interval = [5, 7]
        expected = [[5, 7]]
        self.assertEqual(
            self.solution.insert(intervals.copy(), new_interval.copy()),
            expected
        )

    def test_insert_at_start(self):
        """Test inserting before all existing intervals"""
        intervals = [[3, 5], [6, 8]]
        new_interval = [1, 2]
        expected = [[1, 2], [3, 5], [6, 8]]
        self.assertEqual(
            self.solution.insert(intervals.copy(), new_interval.copy()),
            expected
        )

    def test_insert_at_end(self):
        """Test inserting after all existing intervals"""
        intervals = [[1, 2], [3, 5]]
        new_interval = [6, 8]
        expected = [[1, 2], [3, 5], [6, 8]]
        self.assertEqual(
            self.solution.insert(intervals.copy(), new_interval.copy()),
            expected
        )

    def test_complete_overlap(self):
        """Test when new interval completely overlaps an existing one"""
        intervals = [[1, 2], [3, 4], [5, 6]]
        new_interval = [2, 5]
        expected = [[1, 6]]
        self.assertEqual(
            self.solution.insert(intervals.copy(), new_interval.copy()),
            expected
        )

    def test_no_overlap(self):
        """Test when new interval doesn't overlap with any existing ones"""
        intervals = [[1, 2], [4, 5], [7, 8]]
        new_interval = [3, 3]
        expected = [[1, 2], [3, 3], [4, 5], [7, 8]]
        self.assertEqual(
            self.solution.insert(intervals.copy(), new_interval.copy()),
            expected
        )

    def test_single_point_overlap(self):
        """Test when new interval touches existing intervals at endpoints"""
        intervals = [[1, 3], [6, 9]]
        new_interval = [3, 6]
        expected = [[1, 9]]
        self.assertEqual(
            self.solution.insert(intervals.copy(), new_interval.copy()),
            expected
        )

    def test_negative_numbers(self):
        """Test with negative numbers in intervals"""
        intervals = [[-5, -3], [0, 2], [4, 6]]
        new_interval = [-2, 1]
        expected = [[-5, -3], [-2, 2], [4, 6]]
        self.assertEqual(
            self.solution.insert(intervals.copy(), new_interval.copy()),
            expected
        )

    def test_large_numbers(self):
        """Test with large numbers in intervals"""
        intervals = [[1, 1000], [2000, 3000]]
        new_interval = [900, 2100]
        expected = [[1, 3000]]
        self.assertEqual(
            self.solution.insert(intervals.copy(), new_interval.copy()),
            expected
        )


class TestInsertIntervalLinearSearch(TestInsertIntervalBase, unittest.TestCase):
    """Test cases for linear search implementation"""
    def get_solution(self):
        return SolutionLinearSearch()


class TestInsertIntervalBinarySearch(TestInsertIntervalBase, unittest.TestCase):
    """Test cases for binary search implementation"""
    def get_solution(self):
        return SolutionBinarySearch()

    def test_input_modification(self):
        """Test that binary search implementation modifies input as expected"""
        intervals = [[1, 3], [6, 9]]
        new_interval = [2, 5]
        original = intervals.copy()
        self.solution.insert(intervals, new_interval)
        self.assertNotEqual(intervals, original)


if __name__ == "__main__":
    unittest.main()
