import unittest
from .isomorphic_strings import (
    SolutionCharacterMappingWithDictionary,
    SolutionFirstOccurenceTransformation,
)


class BaseTestIsomorphicStrings:
    """Base test class for isomorphic strings solutions"""

    def setUp(self):
        self.solution = self.SolutionClass()

    def test_basic_isomorphic(self):
        """Test basic isomorphic cases"""
        self.assertTrue(self.solution.isIsomorphic("egg", "add"))
        self.assertTrue(self.solution.isIsomorphic("paper", "title"))
        self.assertTrue(self.solution.isIsomorphic("a", "b"))

    def test_non_isomorphic(self):
        """Test non-isomorphic cases"""
        self.assertFalse(self.solution.isIsomorphic("foo", "bar"))
        self.assertFalse(self.solution.isIsomorphic("badc", "baba"))
        self.assertFalse(self.solution.isIsomorphic("aaab", "aabb"))

    def test_edge_cases(self):
        """Test edge cases"""
        self.assertTrue(self.solution.isIsomorphic("", ""))  # Empty strings
        self.assertTrue(self.solution.isIsomorphic("a", "a"))  # Same single char
        self.assertFalse(self.solution.isIsomorphic("a", "aa"))  # Different lengths

    def test_same_structure_diff_chars(self):
        """Test same character structure with different mappings"""
        self.assertTrue(self.solution.isIsomorphic("abcdef", "ghijkl"))
        self.assertFalse(self.solution.isIsomorphic("abba", "abab"))

    def test_full_alphabet(self):
        """Test maximum unique character scenarios"""
        s = "abcdefghijklmnopqrstuvwxyz"
        t = "zyxwvutsrqponmlkjihgfedcba"
        self.assertTrue(self.solution.isIsomorphic(s, t))


class TestCharacterMappingSolution(BaseTestIsomorphicStrings, unittest.TestCase):
    SolutionClass = SolutionCharacterMappingWithDictionary


class TestFirstOccurenceSolution(BaseTestIsomorphicStrings, unittest.TestCase):
    SolutionClass = SolutionFirstOccurenceTransformation


if __name__ == "__main__":
    unittest.main()
