import unittest
from typing import List, Type
import time

from dp.best_sightseeing_pair import SolutionDP, SolutionSpaceOptimizedDP


class TestMaxScoreSightseeingPair(unittest.TestCase):
    def setUp(self):
        """Initialize solution instances before each test"""
        self.solutions = [SolutionDP(), SolutionSpaceOptimizedDP()]

    def run_test_for_all_solutions(
        self, values: List[int], expected: int, test_name: str
    ):
        """Helper method to run a test case for all solution classes"""
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__):
                result = solution.maxScoreSightseeingPair(values)
                self.assertEqual(
                    result,
                    expected,
                    f"{test_name} failed for {solution.__class__.__name__}: "
                    f"Expected {expected}, got {result}",
                )

    def test_example_case(self):
        """Test the example case given in the problem"""
        values = [8, 1, 5, 2, 6]
        expected = 11  # pairs (0,2) give max score: values[0] + values[2] + 0 - 2 = 8 + 5 - 2 = 11
        self.run_test_for_all_solutions(values, expected, "Example case")

    def test_minimum_length(self):
        """Test with array of minimum length (2 elements)"""
        values = [1, 2]
        expected = 2  # Only one possible pair
        self.run_test_for_all_solutions(values, expected, "Minimum length")

    def test_descending_values(self):
        """Test with array of descending values"""
        values = [10, 8, 6, 4, 2]
        expected = 17  # pairs (0,1) give max score: 10 + 8 - 1 = 17
        self.run_test_for_all_solutions(values, expected, "Descending values")

    def test_ascending_values(self):
        """Test with array of ascending values"""
        values = [1, 3, 5, 7, 9]
        expected = 15  # Consider distance penalty
        self.run_test_for_all_solutions(values, expected, "Ascending values")

    def test_same_values(self):
        """Test with array of same values"""
        values = [5, 5, 5, 5, 5]
        expected = 9  # Any adjacent pair gives same score due to distance penalty
        self.run_test_for_all_solutions(values, expected, "Same values")

    def test_alternating_values(self):
        """Test with alternating high and low values"""
        values = [1, 10, 1, 10, 1]
        expected = 18  # pairs (1,3) give max score
        self.run_test_for_all_solutions(values, expected, "Alternating values")

    def test_large_distance_penalty(self):
        """Test where distance penalty significantly affects the score"""
        values = [10, 1, 1, 1, 1, 1, 1, 1, 1, 20]
        expected = 21  # Despite 20 being highest, distance penalty makes it suboptimal
        self.run_test_for_all_solutions(values, expected, "Large distance penalty")

    def test_single_peak(self):
        """Test with a single peak in the middle"""
        values = [1, 2, 10, 2, 1]
        expected = 11
        self.run_test_for_all_solutions(values, expected, "Single peak")

    def test_performance_comparison(self):
        """Compare performance of different solutions with a large input"""
        large_input = [
            i % 10 for i in range(10000)
        ]  # Large array with repeating pattern

        results = {}
        times = {}

        print("\nPerformance comparison:")
        for solution in self.solutions:
            start_time = time.time()
            result = solution.maxScoreSightseeingPair(large_input)
            end_time = time.time()

            solution_name = solution.__class__.__name__
            results[solution_name] = result
            times[solution_name] = end_time - start_time

            print(f"{solution_name}: {times[solution_name]:.4f} seconds")

        # Verify all solutions give same result
        first_result = next(iter(results.values()))
        for solution_name, result in results.items():
            self.assertEqual(
                result,
                first_result,
                f"Inconsistent results: {solution_name} gave different answer",
            )

    def test_edge_values(self):
        """Test with edge case values (very large numbers)"""
        values = [1000000] * 5
        expected = 1999999  # Max possible score with these values
        self.run_test_for_all_solutions(values, expected, "Edge values")

    def test_negative_impact(self):
        """Test where negative impact of distance might exceed positive values"""
        values = [1, 1, 1, 1, 10]
        expected = 10  # Despite 10 being highest, distance penalty is significant
        self.run_test_for_all_solutions(values, expected, "Negative impact")


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
