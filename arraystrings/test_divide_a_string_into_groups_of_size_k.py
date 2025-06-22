import unittest
import sys
import os

# Add the parent directory to the path to import the Solution class
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from arraystrings.divide_a_string_into_groups_of_size_k import Solution


class TestDivideString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        """Test with empty string"""
        self.assertEqual(self.solution.divideString("", 3, "x"), [])
        self.assertEqual(self.solution.divideString("", 1, "x"), [])

    def test_string_length_equals_k(self):
        """Test when string length equals k"""
        self.assertEqual(self.solution.divideString("abc", 3, "x"), ["abc"])
        self.assertEqual(self.solution.divideString("a", 1, "x"), ["a"])

    def test_string_length_less_than_k(self):
        """Test when string length is less than k"""
        self.assertEqual(self.solution.divideString("ab", 3, "x"), ["abx"])
        self.assertEqual(self.solution.divideString("a", 2, "x"), ["ax"])
        self.assertEqual(self.solution.divideString("", 2, "x"), [])

    def test_string_length_greater_than_k(self):
        """Test when string length is greater than k"""
        # Length 4, k=2: should give ["ab", "cd"]
        self.assertEqual(self.solution.divideString("abcd", 2, "x"), ["ab", "cd"])

        # Length 5, k=2: should give ["ab", "cd", "ex"]
        self.assertEqual(
            self.solution.divideString("abcde", 2, "x"), ["ab", "cd", "ex"]
        )

        # Length 6, k=2: should give ["ab", "cd", "ef"]
        self.assertEqual(
            self.solution.divideString("abcdef", 2, "x"), ["ab", "cd", "ef"]
        )

    def test_string_length_multiple_of_k(self):
        """Test when string length is a multiple of k"""
        self.assertEqual(self.solution.divideString("abcdef", 3, "x"), ["abc", "def"])
        self.assertEqual(
            self.solution.divideString("abcdefgh", 4, "x"), ["abcd", "efgh"]
        )
        self.assertEqual(self.solution.divideString("ab", 1, "x"), ["a", "b"])

    def test_string_length_not_multiple_of_k(self):
        """Test when string length is not a multiple of k"""
        # Length 7, k=3: should give ["abc", "def", "gxx"]
        self.assertEqual(
            self.solution.divideString("abcdefg", 3, "x"), ["abc", "def", "gxx"]
        )

        # Length 8, k=3: should give ["abc", "def", "ghx"]
        self.assertEqual(
            self.solution.divideString("abcdefgh", 3, "x"), ["abc", "def", "ghx"]
        )

    def test_different_fill_characters(self):
        """Test with different fill characters"""
        self.assertEqual(self.solution.divideString("ab", 3, "0"), ["ab0"])
        self.assertEqual(self.solution.divideString("ab", 3, "*"), ["ab*"])
        self.assertEqual(self.solution.divideString("ab", 3, " "), ["ab "])
        self.assertEqual(self.solution.divideString("ab", 3, ""), ["ab"])

    def test_k_equals_one(self):
        """Test when k equals 1"""
        self.assertEqual(self.solution.divideString("abc", 1, "x"), ["a", "b", "c"])
        self.assertEqual(self.solution.divideString("a", 1, "x"), ["a"])
        self.assertEqual(self.solution.divideString("", 1, "x"), [])

    def test_large_k(self):
        """Test with large k values"""
        self.assertEqual(self.solution.divideString("abc", 5, "x"), ["abcxx"])
        self.assertEqual(
            self.solution.divideString("abcdefgh", 10, "x"), ["abcdefghxx"]
        )

    def test_leetcode_examples(self):
        """Test with LeetCode example cases"""
        # Example 1: s = "abcdefghi", k = 3, fill = "x"
        # Output: ["abc","def","ghi"]
        self.assertEqual(
            self.solution.divideString("abcdefghi", 3, "x"), ["abc", "def", "ghi"]
        )

        # Example 2: s = "abcdefghij", k = 3, fill = "x"
        # Output: ["abc","def","ghi","jxx"]
        self.assertEqual(
            self.solution.divideString("abcdefghij", 3, "x"),
            ["abc", "def", "ghi", "jxx"],
        )

    def test_edge_cases(self):
        """Test various edge cases"""
        # Single character with k=1
        self.assertEqual(self.solution.divideString("a", 1, "x"), ["a"])

        # Empty string with k=1
        self.assertEqual(self.solution.divideString("", 1, "x"), [])

        # String shorter than k
        self.assertEqual(self.solution.divideString("hi", 4, "x"), ["hixx"])

        # String exactly k characters
        self.assertEqual(self.solution.divideString("hi", 2, "x"), ["hi"])

    def test_special_characters(self):
        """Test with special characters"""
        self.assertEqual(
            self.solution.divideString("a@b#c", 2, "x"), ["a@", "b#", "cx"]
        )
        self.assertEqual(self.solution.divideString("123", 2, "0"), ["12", "30"])

    def test_numbers_and_symbols(self):
        """Test with numbers and symbols"""
        self.assertEqual(
            self.solution.divideString("12345", 2, "0"), ["12", "34", "50"]
        )
        self.assertEqual(self.solution.divideString("!@#$%", 3, "*"), ["!@#", "$%*"])

    def test_unicode_characters(self):
        """Test with unicode characters"""
        self.assertEqual(
            self.solution.divideString("你好世界", 2, "x"), ["你好", "世界"]
        )
        self.assertEqual(self.solution.divideString("你好", 3, "x"), ["你好x"])

    def test_mixed_content(self):
        """Test with mixed content (letters, numbers, symbols)"""
        self.assertEqual(
            self.solution.divideString("a1b2c3", 2, "x"), ["a1", "b2", "c3"]
        )
        self.assertEqual(
            self.solution.divideString("a1b2c", 2, "x"), ["a1", "b2", "cx"]
        )

    def test_whitespace_handling(self):
        """Test with whitespace characters"""
        self.assertEqual(
            self.solution.divideString("a b c", 2, "x"), ["a ", "b ", "cx"]
        )
        self.assertEqual(self.solution.divideString("  ", 1, "x"), [" ", " "])

    def test_zero_k_edge_case(self):
        """Test edge case with k=0 (should handle gracefully)"""
        # This is an edge case - k=0 doesn't make much sense for this function
        # The function should handle it gracefully or raise an appropriate error
        try:
            result = self.solution.divideString("abc", 0, "x")
            # If it doesn't raise an error, we should test the result
            self.assertIsInstance(result, list)
        except (ValueError, ZeroDivisionError):
            # If it raises an error, that's also acceptable behavior
            pass


if __name__ == "__main__":
    unittest.main()
