import unittest
from backtracking.the_k_th_lexicographical_string_of_all_happy_strings_of_length_n import (
    Solution,
)


class TestKthLexicographicalHappyString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test with n=1, k=3: should return 'c'"""
        self.assertEqual(self.solution.getHappyString(n=1, k=3), "c")

    def test_example_2(self):
        """Test with n=1, k=4: should return empty string as k exceeds possible combinations"""
        self.assertEqual(self.solution.getHappyString(n=1, k=4), "")

    def test_example_3(self):
        """Test with n=3, k=9: should return 'cab'"""
        self.assertEqual(self.solution.getHappyString(n=3, k=9), "cab")

    def test_length_2_first_string(self):
        """Test first string with length 2: should return 'ab'"""
        self.assertEqual(self.solution.getHappyString(n=2, k=1), "ab")

    def test_length_2_last_string(self):
        """Test last string with length 2: should return 'cb'"""
        self.assertEqual(self.solution.getHappyString(n=2, k=6), "cb")

    def test_invalid_k(self):
        """Test with k larger than possible combinations: should return empty string"""
        self.assertEqual(self.solution.getHappyString(n=2, k=7), "")

    def test_length_3_middle_string(self):
        """Test middle string with length 3: should return 'bab'"""
        self.assertEqual(self.solution.getHappyString(n=3, k=5), "bab")


if __name__ == "__main__":
    unittest.main()
