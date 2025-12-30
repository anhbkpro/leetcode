import unittest
from typing import List

from .contains_duplicate_ii import SolutionDictionary, SolutionSlidingWindow


class BaseTestContainsDuplicateII:
    """Base test class for contains duplicate II solutions"""

    def test_contains_nearby_duplicate(self):
        """Test basic functionality"""
        solution = self.SolutionClass()
        test_cases = [
            ([1, 2, 3, 1], 3, True),
            ([1, 0, 1, 1], 1, True),
            ([1, 2, 3, 1, 2, 3], 2, False),
            ([], 0, False),
            ([5], 0, False),
            ([-1, -1], 1, True),
            ([0, 0], 0, False),
            ([0, 1, 0], 1, False),
            ([0, 1, 0], 2, True),
            (list(range(10000)) + [9999], 1, True),
        ]

        for nums, k, expected in test_cases:
            with self.subTest(nums=nums, k=k):
                self.assertEqual(solution.containsNearbyDuplicate(nums, k), expected)


class TestSlidingWindowSolution(BaseTestContainsDuplicateII, unittest.TestCase):
    SolutionClass = SolutionSlidingWindow


class TestDictionarySolution(BaseTestContainsDuplicateII, unittest.TestCase):
    SolutionClass = SolutionDictionary


if __name__ == "__main__":
    unittest.main()
