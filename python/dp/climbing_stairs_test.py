from typing import Type
import unittest
from .climbing_stairs import SolutionBase, SolutionDP, SolutionRecursionMemoization


class TestClimbingStairs(unittest.TestCase):
    def run_test_case(self, solution_class: Type[SolutionBase], n: int, expected: int):
        """Helper method to run a test case for a specific solution class"""
        solution = solution_class()
        result = solution.climbStairs(n)
        self.assertEqual(
            result,
            expected,
            f"{solution_class.__name__} failed: Expected {expected}, got {result}",
        )

    def run_all_solutions(self, n: int, expected: int):
        """Run the same test case for all solution classes"""
        solutions = [SolutionDP, SolutionRecursionMemoization]
        for solution_class in solutions:
            self.run_test_case(solution_class, n, expected)

    def test_base_cases(self):
        """Test with the base cases for the number of ways to climb stairs"""
        self.run_all_solutions(0, 1)
        self.run_all_solutions(1, 1)
        self.run_all_solutions(2, 2)

    def test_example_case(self):
        """Test the example case given in the problem description"""
        self.run_all_solutions(3, 3)

    def test_multiple_ways(self):
        """Test with a number of stairs that can be climbed in multiple ways"""
        self.run_all_solutions(4, 5)

    def test_large_number(self):
        """Test with a large number of stairs"""
        self.run_all_solutions(10, 89)

    def test_very_large_number(self):
        """Test with a very large number of stairs"""
        self.run_all_solutions(30, 1346269)
