import unittest

from .meeting_rooms_ii import SolutionChronologicalOrdering, SolutionPriorityQueues


class BaseTestMeetingRoomsII:
    def setUp(self):
        self.solution = None

    def test_both_solutions_example_1(self):
        intervals = [[0, 30], [5, 10], [15, 20]]
        expected = 2
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_both_solutions_example_2(self):
        intervals = [[7, 10], [2, 4]]
        expected = 1
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_both_solutions_empty_intervals(self):
        intervals = []
        expected = 0
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_both_solutions_single_meeting(self):
        intervals = [[1, 5]]
        expected = 1
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_both_solutions_concurrent_meetings(self):
        intervals = [[1, 4], [1, 4], [1, 4]]
        expected = 3
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_both_solutions_partial_overlaps(self):
        intervals = [[0, 10], [5, 15], [10, 20], [15, 25]]
        expected = 2
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_both_solutions_no_overlap(self):
        intervals = [[1, 3], [4, 6], [7, 9], [10, 12]]
        expected = 1
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_both_solutions_nested_meetings(self):
        intervals = [[1, 10], [2, 5], [3, 4]]
        expected = 3
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_both_solutions_adjacent_meetings(self):
        intervals = [[1, 5], [5, 10], [10, 15]]
        expected = 1
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)


class TestMeetingRoomsIIPriorityQueues(BaseTestMeetingRoomsII, unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.solution = SolutionPriorityQueues()


class TestMeetingRoomsIIChronologicalOrdering(
    BaseTestMeetingRoomsII, unittest.TestCase
):
    def setUp(self):
        super().setUp()
        self.solution = SolutionChronologicalOrdering()


if __name__ == "__main__":
    unittest.main()
