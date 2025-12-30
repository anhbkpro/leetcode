import unittest

from .count_days_without_meetings import Solution


class TestCountDays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_no_meetings(self):
        # Test case with no meetings
        days = 5
        meetings = []
        expected = 5  # All days are free
        result = self.solution.countDays(days, meetings)
        self.assertEqual(result, expected)

    def test_single_meeting(self):
        # Test case with a single meeting
        days = 5
        meetings = [[2, 3]]  # Meeting on days 2-3
        expected = 3  # Days 1, 4, and 5 are free
        result = self.solution.countDays(days, meetings)
        self.assertEqual(result, expected)

    def test_multiple_meetings_no_overlap(self):
        # Test case with multiple non-overlapping meetings
        days = 10
        meetings = [[1, 2], [4, 5], [7, 8]]  # Three separate meetings
        expected = 4  # Days 3, 6, 9, 10 are free
        result = self.solution.countDays(days, meetings)
        self.assertEqual(result, expected)

    def test_overlapping_meetings(self):
        # Test case with overlapping meetings
        days = 5
        meetings = [
            [1, 3],  # Meeting covering days 1-3
            [2, 4],  # Meeting covering days 2-4
        ]
        expected = 1  # Only day 5 is free
        result = self.solution.countDays(days, meetings)
        self.assertEqual(result, expected)

    def test_meetings_with_gaps(self):
        # Test case with meetings having gaps between them
        days = 10
        meetings = [[2, 3], [6, 8]]  # Two meetings with gaps
        expected = 5  # Days 1, 4, 5, 9, 10 are free
        result = self.solution.countDays(days, meetings)
        self.assertEqual(result, expected)

    def test_back_to_back_meetings(self):
        # Test case with consecutive meetings
        days = 6
        meetings = [[1, 2], [3, 4], [5, 6]]  # No gaps between meetings
        expected = 0  # No free days
        result = self.solution.countDays(days, meetings)
        self.assertEqual(result, expected)

    def test_single_day_meetings(self):
        # Test case with single-day meetings
        days = 5
        meetings = [[1, 1], [3, 3], [5, 5]]  # One-day meetings
        expected = 2  # Days 2 and 4 are free
        result = self.solution.countDays(days, meetings)
        self.assertEqual(result, expected)

    def test_complete_coverage(self):
        # Test case where meetings cover all days
        days = 3
        meetings = [[1, 3]]  # One meeting covering all days
        expected = 0  # No free days
        result = self.solution.countDays(days, meetings)
        self.assertEqual(result, expected)

    def test_meetings_with_large_gaps(self):
        # Test case with large gaps between meetings
        days = 10
        meetings = [[1, 1], [10, 10]]  # Meetings on first and last day
        expected = 8  # Days 2-9 are free
        result = self.solution.countDays(days, meetings)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
