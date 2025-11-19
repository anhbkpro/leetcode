import unittest
from .meeting_rooms_iii import Solution


class TestMeetingRoomsIII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 2
        meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
        expected = 0
        self.assertEqual(self.solution.mostBooked(n, meetings), expected)

    def test_example_2(self):
        n = 3
        meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
        expected = 1
        self.assertEqual(self.solution.mostBooked(n, meetings), expected)

    def test_single_room(self):
        n = 1
        meetings = [[0, 5], [5, 10], [10, 15]]
        expected = 0
        self.assertEqual(self.solution.mostBooked(n, meetings), expected)

    def test_empty_meetings(self):
        n = 2
        meetings = []
        expected = 0
        self.assertEqual(self.solution.mostBooked(n, meetings), expected)

    def test_single_meeting(self):
        n = 3
        meetings = [[1, 5]]
        expected = 0
        self.assertEqual(self.solution.mostBooked(n, meetings), expected)

    def test_all_rooms_used_equally(self):
        n = 3
        meetings = [[0, 5], [0, 5], [0, 5]]
        expected = 0
        self.assertEqual(self.solution.mostBooked(n, meetings), expected)

    def test_delayed_meetings(self):
        n = 2
        meetings = [[0, 10], [1, 2], [2, 3], [3, 4]]
        expected = 1
        self.assertEqual(self.solution.mostBooked(n, meetings), expected)

    def test_long_meetings(self):
        n = 2
        meetings = [[0, 100], [1, 2], [2, 3], [3, 4]]
        expected = 1
        self.assertEqual(self.solution.mostBooked(n, meetings), expected)

    def test_concurrent_start_times(self):
        n = 3
        meetings = [[0, 5], [0, 10], [0, 15]]
        expected = 0
        self.assertEqual(self.solution.mostBooked(n, meetings), expected)

    def test_large_gaps_between_meetings(self):
        n = 2
        meetings = [[0, 5], [10, 15], [20, 25]]
        expected = 0
        self.assertEqual(self.solution.mostBooked(n, meetings), expected)


if __name__ == "__main__":
    unittest.main()
