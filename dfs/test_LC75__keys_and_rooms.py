import unittest
from .LC75__keys_and_rooms import Solution


class TestKeysAndRooms(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        rooms = [[1], [2], [3], []]
        expected = True
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_cannot_visit_all(self):
        rooms = [[1, 3], [3, 0, 1], [2], [0]]
        expected = False
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_single_room(self):
        rooms = [[]]
        expected = True
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_two_rooms_connected(self):
        rooms = [[1], []]
        expected = True
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_two_rooms_disconnected(self):
        rooms = [[], [0]]
        expected = False
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_cycle_in_rooms(self):
        rooms = [[1], [2], [0]]
        expected = True
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_multiple_keys_per_room(self):
        rooms = [[1, 2], [2, 3], [3], []]
        expected = True
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_leetcode_example(self):
        rooms = [[1], [2], [3], []]
        expected = True
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_complex_case(self):
        rooms = [[1, 2, 3], [2], [3], []]
        expected = True
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_disconnected_rooms(self):
        rooms = [[1], [2], [], [3]]
        expected = False
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_self_loop(self):
        rooms = [[0], [1], [2]]
        expected = True
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_empty_rooms(self):
        rooms = []
        expected = True
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_large_number_of_rooms(self):
        # Test with 1000 rooms (all connected)
        rooms = [[i + 1] for i in range(999)] + [[]]
        expected = True
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_rooms_with_duplicate_keys(self):
        rooms = [[1, 1, 2], [2, 2], [3], []]
        expected = True
        self.assertEqual(self.solution.canVisitAllRooms(rooms), expected)

    def test_rooms_with_invalid_keys(self):
        rooms = [[1, 5], [2], [3], []]
        with self.assertRaises(IndexError):
            self.solution.canVisitAllRooms(rooms)


if __name__ == "__main__":
    unittest.main()
