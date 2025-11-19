import unittest
from typing import List, Type

from dp.target_sum import SolutionBase, SolutionBF, SolutionMemoization


class TestTargetSumWays(unittest.TestCase):
    def run_test_case(
        self,
        solution_class: Type[SolutionBase],
        nums: List[int],
        target: int,
        expected: int,
    ):
        """Helper method to run a test case for a specific solution class"""
        solution = solution_class()
        result = solution.findTargetSumWays(nums, target)
        self.assertEqual(
            result,
            expected,
            f"{solution_class.__name__} failed: Expected {expected}, got {result}",
        )

    def run_all_solutions(self, nums: List[int], target: int, expected: int):
        """Run the same test case for all solution classes"""
        solutions = [SolutionBF, SolutionMemoization]
        for solution_class in solutions:
            self.run_test_case(solution_class, nums, target, expected)

    def test_basic_example(self):
        """Test with a basic example where there are multiple ways to reach target"""
        nums = [1, 1, 1, 1, 1]
        target = 3
        self.run_all_solutions(nums, target, 5)

    def test_single_number(self):
        """Test with a single number where target can be reached in exactly one way"""
        nums = [5]
        target = 5
        self.run_all_solutions(nums, target, 1)

    def test_no_solution(self):
        """Test when target cannot be reached"""
        nums = [1, 2, 3]
        target = 10
        self.run_all_solutions(nums, target, 0)

    def test_zero_target(self):
        """Test with target of zero"""
        nums = [1, 0]
        target = 0
        self.run_all_solutions(nums, target, 0)

    def test_negative_target(self):
        """Test with negative target value"""
        nums = [1, 2, 1]
        target = -2
        self.run_all_solutions(nums, target, 2)

    def test_large_numbers(self):
        """Test with larger numbers"""
        nums = [10, 20, 30]
        target = 60
        self.run_all_solutions(nums, target, 1)

    def test_multiple_calls(self):
        """Test that multiple calls work correctly"""
        solutions = [SolutionBF, SolutionMemoization]
        for solution_class in solutions:
            solution = solution_class()

            nums1, target1 = [1, 1], 0
            nums2, target2 = [1, 2], 3

            result1 = solution.findTargetSumWays(nums1, target1)
            result2 = solution.findTargetSumWays(nums2, target2)

            self.assertEqual(result1, 2, f"{solution_class.__name__} failed first call")
            self.assertEqual(
                result2, 1, f"{solution_class.__name__} failed second call"
            )

    def test_all_zeros(self):
        """Test with array containing all zeros"""
        nums = [0, 0, 0]
        target = 0
        self.run_all_solutions(nums, target, 8)

    def test_empty_array(self):
        """Test with empty array"""
        nums = []
        target = 0
        self.run_all_solutions(nums, target, 1)

    def test_large_array(self):
        """Test with a larger array"""
        nums = [1] * 10  # Array of 10 ones
        target = 0
        self.run_all_solutions(nums, target, 252)

    def test_max_sum_target(self):
        """Test with target equal to maximum possible sum"""
        nums = [1, 2, 3]
        target = 6
        self.run_all_solutions(nums, target, 1)

    def test_min_sum_target(self):
        """Test with target equal to minimum possible sum"""
        nums = [1, 2, 3]
        target = -6
        self.run_all_solutions(nums, target, 1)

    def test_performance_comparison(self):
        """Optional test to compare performance between solutions"""
        import time

        nums = [1] * 15  # Larger input for noticeable difference
        target = 0

        solutions = [SolutionBF, SolutionMemoization]
        times = {}

        for solution_class in solutions:
            solution = solution_class()
            start_time = time.time()
            result = solution.findTargetSumWays(nums, target)
            end_time = time.time()
            times[solution_class.__name__] = end_time - start_time

        print("\nPerformance comparison:")
        for solution_name, execution_time in times.items():
            print(f"{solution_name}: {execution_time:.4f} seconds")


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
