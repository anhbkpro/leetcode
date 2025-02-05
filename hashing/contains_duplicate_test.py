import unittest
from typing import List
from .contains_duplicate import SolutionHashMap, SolutionSorting


class BaseTestContainsDuplicate:
    """Base test class for contains duplicate solutions"""

    def test_contains_duplicate(self):
        """Test basic functionality"""
        solution = self.SolutionClass()
        test_cases = [
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
            ([], False),
            ([5], False),
            ([-1, -1, 2], True),
            ([0, 0], True),
            (list(range(100000)) + [99999], True),
        ]

        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                self.assertEqual(solution.containsDuplicate(nums), expected)


class TestHashMapSolution(BaseTestContainsDuplicate, unittest.TestCase):
    SolutionClass = SolutionHashMap


class TestSortingSolution(BaseTestContainsDuplicate, unittest.TestCase):
    SolutionClass = SolutionSorting


if __name__ == "__main__":
    unittest.main()
