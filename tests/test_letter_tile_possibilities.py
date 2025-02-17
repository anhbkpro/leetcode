import unittest
from backtracking.letter_tile_possibilities import Solution

class TestLetterTilePossibilities(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        """Test with empty string should return 0"""
        self.assertEqual(self.solution.numTilePossibilities(""), 0)

    def test_single_character(self):
        """Test with single character should return 1"""
        self.assertEqual(self.solution.numTilePossibilities("A"), 1)

    def test_two_different_characters(self):
        """Test with two different characters 'AB' should return 3 ('A', 'B', 'AB', 'BA')"""
        self.assertEqual(self.solution.numTilePossibilities("AB"), 4)

    def test_repeated_characters(self):
        """Test with repeated characters 'AAB' should handle duplicates correctly"""
        self.assertEqual(self.solution.numTilePossibilities("AAB"), 8)

    def test_example_case(self):
        """Test the example case 'AAABBC'"""
        self.assertEqual(self.solution.numTilePossibilities("AAABBC"), 188)

if __name__ == '__main__':
    unittest.main()
