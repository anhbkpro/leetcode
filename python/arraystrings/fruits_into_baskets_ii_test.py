import unittest

from arraystrings.fruits_into_baskets_ii import Solution


class TestFruitsIntoBasketsII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test Example 1 from the problem description"""
        fruits = [4, 2, 5]
        baskets = [3, 5, 4]
        expected = 1
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_example_2(self):
        """Test Example 2 from the problem description"""
        fruits = [3, 6, 1]
        baskets = [6, 4, 7]
        expected = 0
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_all_fruits_placed(self):
        """Test case where all fruits can be placed"""
        fruits = [1, 2, 3]
        baskets = [3, 2, 1]
        expected = 1
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_no_fruits_placed(self):
        """Test case where no fruits can be placed"""
        fruits = [5, 6, 7]
        baskets = [1, 2, 3]
        expected = 3
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_single_fruit_single_basket(self):
        """Test case with single fruit and single basket"""
        fruits = [3]
        baskets = [5]
        expected = 0
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_single_fruit_single_basket_insufficient(self):
        """Test case with single fruit and single basket (insufficient capacity)"""
        fruits = [5]
        baskets = [3]
        expected = 1
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_exact_capacity_match(self):
        """Test case where fruit quantities exactly match basket capacities"""
        fruits = [3, 4, 5]
        baskets = [3, 4, 5]
        expected = 0
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_large_numbers(self):
        """Test case with large numbers"""
        fruits = [1000, 500, 750]
        baskets = [1000, 600, 800]
        expected = 0
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_minimum_constraints(self):
        """Test case with minimum constraints (n=1, values=1)"""
        fruits = [1]
        baskets = [1]
        expected = 0
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_maximum_constraints(self):
        """Test case with maximum constraints (n=100, values=1000)"""
        fruits = [1000] * 100
        baskets = [1000] * 100
        expected = 0
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_partial_placement(self):
        """Test case where some fruits are placed and some are not"""
        fruits = [2, 4, 1, 6, 3]
        baskets = [3, 5, 2, 7]
        expected = 1  # Only 4 fruits can be placed, 1 remains unplaced
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_duplicate_fruit_quantities(self):
        """Test case with duplicate fruit quantities"""
        fruits = [3, 3, 3, 5, 5]
        baskets = [3, 4, 5, 6]
        expected = 1  # One fruit of quantity 5 cannot be placed
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_duplicate_basket_capacities(self):
        """Test case with duplicate basket capacities"""
        fruits = [2, 3, 4, 5]
        baskets = [3, 3, 5, 5]
        expected = 0  # All fruits can be placed
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_edge_case_small_differences(self):
        """Test case with very small differences between fruit and basket capacities"""
        fruits = [1000, 999, 998]
        baskets = [1000, 999, 997]
        expected = 1  # One fruit of quantity 998 cannot be placed
        result = self.solution.numOfUnplacedFruits(fruits, baskets)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")


if __name__ == "__main__":
    unittest.main()
