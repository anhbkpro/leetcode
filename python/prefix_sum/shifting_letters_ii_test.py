import unittest

from .shifting_letters_ii import Solution


class TestShiftingLetters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example from problem description"""
        s = "abc"
        shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "ace")

    def test_example_2(self):
        """Test the second example from problem description"""
        s = "dztz"
        shifts = [[0, 0, 0], [1, 1, 1]]
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "catz")

    def test_empty_shifts(self):
        """Test when no shifts are applied"""
        s = "hello"
        shifts = []
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "hello")

    def test_single_character(self):
        """Test with a single character string"""
        s = "a"
        shifts = [[0, 0, 1]]  # Shift forward once
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "b")

        shifts = [[0, 0, 0]]  # Shift backward once
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "z")

    def test_wrap_around(self):
        """Test wrapping around the alphabet"""
        # Forward wrap
        s = "xyz"
        shifts = [[0, 2, 1]]
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "yza")

        # Backward wrap
        s = "abc"
        shifts = [[0, 2, 0]]
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "zab")

    def test_multiple_shifts_same_range(self):
        """Test multiple shifts on the same range"""
        s = "abc"
        shifts = [[0, 2, 1], [0, 2, 1], [0, 2, 1]]  # Shift forward 3 times
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "def")

    def test_overlapping_shifts(self):
        """Test overlapping shift ranges"""
        s = "abcde"
        shifts = [[0, 2, 1], [1, 3, 1], [2, 4, 1]]
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "bdfff")

    def test_opposite_directions(self):
        """Test shifts in opposite directions"""
        s = "abc"
        shifts = [[0, 2, 1], [0, 2, 0]]  # Forward then backward
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "abc")

    def test_single_position_multiple_shifts(self):
        """Test multiple shifts on a single position"""
        s = "a"
        shifts = [[0, 0, 1], [0, 0, 1], [0, 0, 0]]  # Forward twice then backward once
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "b")

    def test_large_number_of_shifts(self):
        """Test with large number of shifts that should wrap around alphabet multiple times"""
        s = "a"
        shifts = (
            [[0, 0, 1]] * 27
        )  # Shift forward 27 times (should wrap around alphabet once plus one more shift)
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "b")

    def test_boundary_shifts(self):
        """Test shifts at string boundaries"""
        s = "abcde"
        shifts = [[0, 0, 1], [4, 4, 1]]  # Shift first and last characters
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "bbcdf")

    def test_zero_length_shift_range(self):
        """Test shifts where start and end index are the same"""
        s = "abc"
        shifts = [[1, 1, 1]]  # Shift only the middle character
        self.assertEqual(self.solution.shiftingLetters(s, shifts), "acc")


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
