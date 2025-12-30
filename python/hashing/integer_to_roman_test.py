import unittest

from .integer_to_roman import SolutionGreedy, SolutionHardcodeDigits


class BaseTestIntegerToRoman:
    """Base test class with common test cases for integer to Roman numeral conversion"""

    def setUp(self):
        self.solution = self.SolutionClass()

    def test_single_digit(self):
        """Test single digit numbers (1-9)"""
        test_cases = [
            (1, "I"),
            (2, "II"),
            (3, "III"),
            (4, "IV"),
            (5, "V"),
            (6, "VI"),
            (7, "VII"),
            (8, "VIII"),
            (9, "IX"),
        ]
        for num, expected in test_cases:
            with self.subTest(num=num):
                self.assertEqual(self.solution.intToRoman(num), expected)

    def test_tens(self):
        """Test numbers in tens (10-99)"""
        test_cases = [
            (10, "X"),
            (20, "XX"),
            (30, "XXX"),
            (40, "XL"),
            (50, "L"),
            (60, "LX"),
            (70, "LXX"),
            (80, "LXXX"),
            (90, "XC"),
            (99, "XCIX"),
        ]
        for num, expected in test_cases:
            with self.subTest(num=num):
                self.assertEqual(self.solution.intToRoman(num), expected)

    def test_hundreds(self):
        """Test numbers in hundreds (100-999)"""
        test_cases = [
            (100, "C"),
            (200, "CC"),
            (300, "CCC"),
            (400, "CD"),
            (500, "D"),
            (600, "DC"),
            (700, "DCC"),
            (800, "DCCC"),
            (900, "CM"),
            (999, "CMXCIX"),
        ]
        for num, expected in test_cases:
            with self.subTest(num=num):
                self.assertEqual(self.solution.intToRoman(num), expected)

    def test_thousands(self):
        """Test numbers in thousands (1000-3999)"""
        test_cases = [
            (1000, "M"),
            (2000, "MM"),
            (3000, "MMM"),
            (3999, "MMMCMXCIX"),
        ]
        for num, expected in test_cases:
            with self.subTest(num=num):
                self.assertEqual(self.solution.intToRoman(num), expected)

    def test_complex_numbers(self):
        """Test complex numbers that use multiple Roman numeral symbols"""
        test_cases = [
            (1994, "MCMXCIV"),  # M=1000 + CM=900 + XC=90 + IV=4
            (2023, "MMXXIII"),  # MM=2000 + XX=20 + III=3
            (3549, "MMMDXLIX"),  # MMM=3000 + D=500 + XL=40 + IX=9
            (2444, "MMCDXLIV"),  # MM=2000 + CD=400 + XL=40 + IV=4
        ]
        for num, expected in test_cases:
            with self.subTest(num=num):
                self.assertEqual(self.solution.intToRoman(num), expected)

    def test_edge_cases(self):
        """Test edge cases and boundary values"""
        test_cases = [
            (1, "I"),  # Minimum valid input
            (3999, "MMMCMXCIX"),  # Maximum valid input
            (49, "XLIX"),  # Multiple subtractive pairs
            (444, "CDXLIV"),  # Triple subtractive pairs
            (999, "CMXCIX"),  # Maximum value less than M
        ]
        for num, expected in test_cases:
            with self.subTest(num=num):
                self.assertEqual(self.solution.intToRoman(num), expected)


class TestIntegerToRomanGreedy(BaseTestIntegerToRoman, unittest.TestCase):
    """Test cases for the greedy solution"""

    SolutionClass = SolutionGreedy


class TestIntegerToRomanHardcoded(BaseTestIntegerToRoman, unittest.TestCase):
    """Test cases for the hardcoded digits solution"""

    SolutionClass = SolutionHardcodeDigits


if __name__ == "__main__":
    unittest.main()
