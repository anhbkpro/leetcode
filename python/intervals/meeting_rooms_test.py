import unittest

from .meeting_rooms import Solution


class TestMeetingRooms(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        intervals = [[0, 30], [5, 10], [15, 20]]
        self.assertFalse(self.solution.canAttendMeetings(intervals))

    def test_example_2(self):
        intervals = [[7, 10], [2, 4]]
        self.assertTrue(self.solution.canAttendMeetings(intervals))

    def test_empty_intervals(self):
        intervals = []
        self.assertTrue(self.solution.canAttendMeetings(intervals))

    def test_single_meeting(self):
        intervals = [[1, 5]]
        self.assertTrue(self.solution.canAttendMeetings(intervals))

    def test_adjacent_meetings(self):
        intervals = [[1, 5], [5, 10], [10, 15]]
        self.assertTrue(self.solution.canAttendMeetings(intervals))

    def test_overlapping_at_start(self):
        intervals = [[1, 5], [2, 6]]
        self.assertFalse(self.solution.canAttendMeetings(intervals))

    def test_overlapping_at_end(self):
        intervals = [[1, 6], [5, 10]]
        self.assertFalse(self.solution.canAttendMeetings(intervals))

    def test_completely_overlapping(self):
        intervals = [[2, 8], [3, 7]]
        self.assertFalse(self.solution.canAttendMeetings(intervals))

    def test_same_time_meetings(self):
        intervals = [[2, 4], [2, 4]]
        self.assertFalse(self.solution.canAttendMeetings(intervals))


if __name__ == "__main__":
    unittest.main()
