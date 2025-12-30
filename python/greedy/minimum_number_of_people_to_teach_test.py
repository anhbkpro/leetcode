import unittest

from greedy.minimum_number_of_people_to_teach import Solution


class TestMinimumTeachings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example from the problem description"""
        n = 2
        languages = [[1], [2], [1, 2]]
        friendships = [[1, 2], [1, 3], [2, 3]]
        expected = 1
        result = self.solution.minimumTeachings(n, languages, friendships)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """Test the second example from the problem description"""
        n = 3
        languages = [[2], [1, 3], [1, 2], [3]]
        friendships = [[1, 4], [1, 2], [3, 4], [2, 3]]
        expected = 2
        result = self.solution.minimumTeachings(n, languages, friendships)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
