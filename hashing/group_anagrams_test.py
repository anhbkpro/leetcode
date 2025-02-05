import unittest
from typing import List
from .group_anagrams import (
    SolutionCategorizeBySortedString,
    SolutionCategorizeByCharacterCount,
)


class BaseTestGroupAnagrams:
    """Base test class for group anagrams solutions"""

    def test_group_anagrams(self):
        """Test basic anagram grouping functionality"""
        solution = self.SolutionClass()
        test_cases = [
            (
                ["eat", "tea", "tan", "ate", "nat", "bat"],
                [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            ),
            ([""], [[""]]),
            (["a"], [["a"]]),
            (
                ["cab", "tin", "pew", "duh", "may", "buy", "doc", "ill"],
                [
                    ["cab"],
                    ["tin"],
                    ["pew"],
                    ["duh"],
                    ["may"],
                    ["buy"],
                    ["doc"],
                    ["ill"],
                ],
            ),
        ]

        for strs, expected in test_cases:
            with self.subTest(strs=strs):
                result = solution.groupAnagrams(strs)
                self.assertEqual(
                    self.normalize_result(result), self.normalize_result(expected)
                )

    def test_edge_cases(self):
        """Test empty input and single element cases"""
        solution = self.SolutionClass()
        self.assertEqual(solution.groupAnagrams([]), [])
        self.assertEqual(solution.groupAnagrams(["a"]), [["a"]])

    def normalize_result(self, result: List[List[str]]) -> List[List[str]]:
        """Normalize the result for order-agnostic comparison"""
        return sorted(sorted(group) for group in result)


class TestSortedKeySolution(BaseTestGroupAnagrams, unittest.TestCase):
    """Test cases for the sorted key solution"""

    SolutionClass = SolutionCategorizeBySortedString


class TestCharacterCountSolution(BaseTestGroupAnagrams, unittest.TestCase):
    """Test cases for the character count solution"""

    SolutionClass = SolutionCategorizeByCharacterCount


if __name__ == "__main__":
    unittest.main()
