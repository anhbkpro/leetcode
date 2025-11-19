from .count_ways_to_build_good_strings import (
    BaseSolution,
    SolutionInterativeDP,
    SolutionRecursiveDP,
)


class TestCountWaysToBuildGoodStrings:
    def run_test_case(
        self,
        solution_class: BaseSolution,
        low: int,
        high: int,
        zero: int,
        one: int,
        expected: int,
    ):
        """Helper method to run a test case for a specific solution class"""
        solution = solution_class()
        result = solution.countGoodStrings(low, high, zero, one)
        assert (
            result == expected
        ), f"{solution_class.__name__} failed: Expected {expected}, got {result}"

    def run_all_solutions(
        self, low: int, high: int, zero: int, one: int, expected: int
    ):
        """Run the same test case for all solution classes"""
        solutions = [SolutionInterativeDP, SolutionRecursiveDP]
        for solution_class in solutions:
            self.run_test_case(solution_class, low, high, zero, one, expected)

    def test_basic_example(self):
        """Test with a basic example"""
        low = 3
        high = 3
        zero = 1
        one = 1
        expected = 8
        self.run_all_solutions(low, high, zero, one, expected)
        low = 2
        high = 3
        zero = 1
        one = 2
        expected = 5
        self.run_all_solutions(low, high, zero, one, expected)
