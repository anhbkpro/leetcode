import unittest
from .tuple_with_same_product import (
    SolutionOptimizedBruteForce,
    SolutionCountProductFrequency,
    SolutionProductFrequencyHashMap,
)


class BaseTestTupleSameProduct:
    """Base test class containing all test cases"""

    def setUp(self):
        self.solution = self.solution_class()

    def test_example_1(self):
        """Test example case from problem statement"""
        nums = [2, 3, 4, 6]
        self.assertEqual(self.solution.tupleSameProduct(nums), 8)

    def test_example_2(self):
        """Test example case from problem statement"""
        nums = [1, 2, 4, 5, 10]
        self.assertEqual(self.solution.tupleSameProduct(nums), 16)

    def test_no_valid_tuples(self):
        """Test when there are no valid tuples"""
        nums = [1, 2, 3]
        self.assertEqual(self.solution.tupleSameProduct(nums), 0)

    def test_multiple_valid_tuples(self):
        """Test when there are multiple valid tuples"""
        nums = [2, 3, 4, 6, 8, 12]
        self.assertEqual(self.solution.tupleSameProduct(nums), 40)

    def test_prime_numbers(self):
        """Test with prime numbers"""
        nums = [2, 3, 5, 7, 11, 13]
        self.assertEqual(self.solution.tupleSameProduct(nums), 0)

    def test_single_element(self):
        """Test with single element"""
        nums = [1]
        self.assertEqual(self.solution.tupleSameProduct(nums), 0)

    def test_large_numbers(self):
        """Test with large numbers"""
        nums = [1000, 2000, 3000, 6000]
        self.assertEqual(self.solution.tupleSameProduct(nums), 8)


class TestSolutionOptimizedBruteForce(BaseTestTupleSameProduct, unittest.TestCase):
    """Test cases for the optimized brute force solution"""

    solution_class = SolutionOptimizedBruteForce


class TestSolutionCountProductFrequency(BaseTestTupleSameProduct, unittest.TestCase):
    """Test cases for the product frequency counting solution"""

    solution_class = SolutionCountProductFrequency


class TestSolutionProductFrequencyHashMap(BaseTestTupleSameProduct, unittest.TestCase):
    """Test cases for the hash map-based solution"""

    solution_class = SolutionProductFrequencyHashMap


if __name__ == "__main__":
    unittest.main()
