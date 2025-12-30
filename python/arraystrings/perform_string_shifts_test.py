import unittest

from .perform_string_shifts import Solution


class TestStringShift(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case from Example 1: s = "abc", shift = [[0,1],[1,2]]"""
        s = "abc"
        shift = [[0, 1], [1, 2]]
        self.assertEqual(self.solution.stringShift(s, shift), "cab")

    def test_example_2(self):
        """Test case from Example 2: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]"""
        s = "abcdefg"
        shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
        self.assertEqual(self.solution.stringShift(s, shift), "efgabcd")

    def test_single_character(self):
        """Test string with single character - any shift should return same string"""
        s = "a"
        shifts = [
            [[0, 1]],  # Left shift
            [[1, 1]],  # Right shift
            [[0, 100]],  # Large left shift
            [[1, 100]],  # Large right shift
        ]
        for shift in shifts:
            self.assertEqual(self.solution.stringShift(s, shift), "a")

    def test_empty_shifts(self):
        """Test with empty shift array - should return original string"""
        s = "hello"
        shift = []
        self.assertEqual(self.solution.stringShift(s, shift), "hello")

    def test_no_effective_shift(self):
        """Test shifts that effectively cancel each other out"""
        s = "hello"
        shift = [[0, 2], [1, 2]]  # Left 2, then right 2
        self.assertEqual(self.solution.stringShift(s, shift), "hello")

    def test_alternating_shifts(self):
        """Test alternating left and right shifts"""
        s = "abcd"
        shift = [[0, 1], [1, 1], [0, 1], [1, 1]]
        self.assertEqual(self.solution.stringShift(s, shift), "abcd")

    def test_consecutive_same_direction(self):
        """Test multiple shifts in same direction"""
        s = "abcd"
        # Three consecutive right shifts
        shift = [[1, 1], [1, 1], [1, 1]]
        self.assertEqual(self.solution.stringShift(s, shift), "bcd" + "a")

    def test_palindrome(self):
        """Test with palindrome string"""
        s = "racecar"
        shifts = [
            [[0, 1]],  # Left shift
            [[1, 1]],  # Right shift
            [[0, 7]],  # Full rotation left
            [[1, 7]],  # Full rotation right
        ]
        for shift in shifts:
            result = self.solution.stringShift(s, shift)
            self.assertEqual(len(result), len(s))
            self.assertTrue(all(c in s for c in result))

    def test_repeated_characters(self):
        """Test string with repeated characters"""
        s = "aaa"
        shifts = [[[0, 1]], [[1, 1]], [[0, 2]], [[1, 2]]]
        for shift in shifts:
            self.assertEqual(self.solution.stringShift(s, shift), "aaa")

    def test_max_constraints(self):
        """Test with maximum constraint values"""
        s = "a" * 100  # Max length string
        shift = [[0, 100]] * 100  # Max shifts with max amount
        self.assertEqual(self.solution.stringShift(s, shift), s)

    def test_multiple_full_rotations(self):
        """Test shifts that result in multiple full rotations"""
        s = "abc"
        shift = [[0, 3], [1, 3], [0, 6], [1, 6]]  # Multiple full rotations
        self.assertEqual(self.solution.stringShift(s, shift), "abc")


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
