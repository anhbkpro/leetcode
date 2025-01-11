import unittest
from .unique_substrings_with_equal_digit_frequency import Solution


class TestEqualDigitFrequency(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example case: s = "1212" """
        result = self.solution.equalDigitFrequency("1212")
        self.assertEqual(result, 5)

    def test_example_2(self):
        """Test the second example case: s = "12321" """
        result = self.solution.equalDigitFrequency("12321")
        self.assertEqual(result, 9)

    def test_single_digit(self):
        """Test with a single digit string"""
        result = self.solution.equalDigitFrequency("1")
        self.assertEqual(result, 1)

    def test_all_same_digits(self):
        """Test with string containing all same digits"""
        result = self.solution.equalDigitFrequency("333")
        self.assertEqual(result, 3)  # "3", "3", "3"

    def test_no_equal_frequency(self):
        """Test with string having no substrings with equal frequency except single digits"""
        result = self.solution.equalDigitFrequency("112")
        self.assertEqual(result, 4)  # Only two "1", one "2", one "12" are valid

    def test_multiple_equal_frequency(self):
        """Test with string having multiple equal frequency substrings"""
        result = self.solution.equalDigitFrequency("11223344")
        expected = set(
            [
                "1",
                "11",
                "1122",
                "112233",
                "11223344",
                "12",
                "2",
                "22",
                "2233",
                "223344",
                "23",
                "3",
                "33",
                "3344",
                "34",
                "4",
                "44",
            ]
        )
        self.assertEqual(result, len(expected))

    def test_max_length(self):
        """Test with a string of maximum allowed length (1000)"""
        s = "12" * 500  # 1000 characters
        result = self.solution.equalDigitFrequency(s)
        self.assertTrue(result > 0)  # At least some valid substrings should exist

    def test_non_digit_string(self):
        """Test with non-digit string (though not allowed by constraints)"""
        with self.assertRaises(Exception):
            self.solution.equalDigitFrequency("abc")


if __name__ == "__main__":
    unittest.main(verbosity=2)
