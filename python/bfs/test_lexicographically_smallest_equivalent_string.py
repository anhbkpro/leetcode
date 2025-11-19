import unittest
from .lexicographically_smallest_equivalent_string import Solution


class TestLexicographicallySmallestEquivalentString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        s1 = "parker"
        s2 = "morris"
        baseStr = "parser"
        expected = "makkek"
        self.assertEqual(
            self.solution.smallestEquivalentString(s1, s2, baseStr), expected
        )

    def test_same_characters(self):
        s1 = "hello"
        s2 = "world"
        baseStr = "hold"
        expected = "hdld"
        self.assertEqual(
            self.solution.smallestEquivalentString(s1, s2, baseStr), expected
        )

    def test_empty_strings(self):
        s1 = ""
        s2 = ""
        baseStr = ""
        expected = ""
        self.assertEqual(
            self.solution.smallestEquivalentString(s1, s2, baseStr), expected
        )

    def test_single_character(self):
        s1 = "a"
        s2 = "b"
        baseStr = "c"
        expected = "c"
        self.assertEqual(
            self.solution.smallestEquivalentString(s1, s2, baseStr), expected
        )

    def test_all_same_characters(self):
        s1 = "aaa"
        s2 = "aaa"
        baseStr = "aaa"
        expected = "aaa"
        self.assertEqual(
            self.solution.smallestEquivalentString(s1, s2, baseStr), expected
        )

    def test_complex_case(self):
        s1 = "leetcode"
        s2 = "programs"
        baseStr = "sourcecode"
        expected = "aauaaaaada"
        self.assertEqual(
            self.solution.smallestEquivalentString(s1, s2, baseStr), expected
        )

    def test_no_equivalents(self):
        s1 = "abc"
        s2 = "def"
        baseStr = "ghi"
        expected = "ghi"
        self.assertEqual(
            self.solution.smallestEquivalentString(s1, s2, baseStr), expected
        )


if __name__ == "__main__":
    unittest.main()
