import unittest

from .ransom_note import (
    SolutionOneHashMap,
    SolutionSimulation,
    SolutionSortingAndStacks,
    SolutionTwoHashMaps,
)


class BaseTestRansomNote:
    """Base test class with common test cases for ransom note construction"""

    def setUp(self):
        self.solution = self.SolutionClass()

    def test_basic_cases(self):
        """Test basic cases with simple strings"""
        test_cases = [
            ("a", "b", False),  # Different single letters
            ("aa", "ab", False),  # Not enough letters
            ("aa", "aab", True),  # Enough letters
            ("abc", "abc", True),  # Exact match
        ]
        for ransomNote, magazine, expected in test_cases:
            with self.subTest(ransomNote=ransomNote, magazine=magazine):
                self.assertEqual(
                    self.solution.canConstruct(ransomNote, magazine), expected
                )

    def test_empty_strings(self):
        """Test cases with empty strings"""
        test_cases = [
            ("", "", True),  # Both empty
            ("", "abc", True),  # Empty note
            ("a", "", False),  # Empty magazine
        ]
        for ransomNote, magazine, expected in test_cases:
            with self.subTest(ransomNote=ransomNote, magazine=magazine):
                self.assertEqual(
                    self.solution.canConstruct(ransomNote, magazine), expected
                )

    def test_repeated_characters(self):
        """Test cases with repeated characters"""
        test_cases = [
            ("aaa", "aaa", True),  # Exact number of repeats
            ("aaa", "aa", False),  # Not enough repeats
            ("aaa", "aaaa", True),  # More than needed
            ("aaab", "aaaa", False),  # Enough of one letter but missing another
        ]
        for ransomNote, magazine, expected in test_cases:
            with self.subTest(ransomNote=ransomNote, magazine=magazine):
                self.assertEqual(
                    self.solution.canConstruct(ransomNote, magazine), expected
                )

    def test_case_sensitivity(self):
        """Test case sensitivity"""
        test_cases = [
            ("a", "A", False),  # Different case
            ("aA", "aA", True),  # Exact case match
            ("aa", "AA", False),  # All caps magazine
            ("AA", "aa", False),  # All caps note
        ]
        for ransomNote, magazine, expected in test_cases:
            with self.subTest(ransomNote=ransomNote, magazine=magazine):
                self.assertEqual(
                    self.solution.canConstruct(ransomNote, magazine), expected
                )

    def test_order_independence(self):
        """Test that letter order doesn't matter"""
        test_cases = [
            ("abc", "cba", True),  # Different order, same letters
            ("hello", "olleh", True),  # Anagrams
            ("world", "dlrow", True),  # Another anagram
            ("paper", "pear", False),  # Similar but insufficient letters
        ]
        for ransomNote, magazine, expected in test_cases:
            with self.subTest(ransomNote=ransomNote, magazine=magazine):
                self.assertEqual(
                    self.solution.canConstruct(ransomNote, magazine), expected
                )

    def test_length_comparison(self):
        """Test cases where length is a factor"""
        test_cases = [
            ("a" * 10, "a" * 5, False),  # Note longer than magazine
            ("a" * 5, "a" * 10, True),  # Magazine longer than note
            ("ab" * 5, "a" * 10, False),  # Same length but different composition
            ("hello", "hheelloo", True),  # Double letters in magazine
        ]
        for ransomNote, magazine, expected in test_cases:
            with self.subTest(ransomNote=ransomNote, magazine=magazine):
                self.assertEqual(
                    self.solution.canConstruct(ransomNote, magazine), expected
                )


class TestRansomNoteSimulation(BaseTestRansomNote, unittest.TestCase):
    """Test cases for the simulation solution"""

    SolutionClass = SolutionSimulation


class TestRansomNoteTwoHashMaps(BaseTestRansomNote, unittest.TestCase):
    """Test cases for the two hash maps solution"""

    SolutionClass = SolutionTwoHashMaps


class TestRansomNoteOneHashMap(BaseTestRansomNote, unittest.TestCase):
    """Test cases for the one hash map solution"""

    SolutionClass = SolutionOneHashMap


class TestRansomNoteSortingAndStacks(BaseTestRansomNote, unittest.TestCase):
    """Test cases for the sorting and stacks solution"""

    SolutionClass = SolutionSortingAndStacks


if __name__ == "__main__":
    unittest.main()
