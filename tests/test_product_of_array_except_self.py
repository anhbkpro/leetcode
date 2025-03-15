import unittest
from prefix_sum.product_of_array_except_self import Solution


class TestProductOfArrayExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_functionality(self):
        # Test basic array with positive numbers
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
        # Test array with ones
        self.assertEqual(self.solution.productExceptSelf([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_edge_cases(self):
        # Test minimum size array (2 elements)
        self.assertEqual(self.solution.productExceptSelf([2, 3]), [3, 2])
        # Test array with zeros
        self.assertEqual(self.solution.productExceptSelf([0, 1, 2, 3]), [6, 0, 0, 0])
        # Test array with multiple zeros
        self.assertEqual(self.solution.productExceptSelf([0, 1, 0, 3]), [0, 0, 0, 0])

    def test_special_cases(self):
        # Test array with negative numbers
        self.assertEqual(
            self.solution.productExceptSelf([-1, -2, -3, -4]), [-24, -12, -8, -6]
        )
        # Test array with mix of positive and negative
        self.assertEqual(
            self.solution.productExceptSelf([-1, 2, -3, 4]), [-24, 12, -8, 6]
        )
        # Test array with alternating numbers
        self.assertEqual(
            self.solution.productExceptSelf([2, -2, 2, -2]), [8, -8, 8, -8]
        )

    def test_boundary_conditions(self):
        # Test array with maximum values
        self.assertEqual(self.solution.productExceptSelf([1000, 1000]), [1000, 1000])
        # Test array with minimum values
        self.assertEqual(
            self.solution.productExceptSelf([-1000, -1000]), [-1000, -1000]
        )
        # Test array with mix of max and min values
        self.assertEqual(
            self.solution.productExceptSelf([-1000, 0, 1000]), [0, -1000000, 0]
        )


if __name__ == "__main__":
    unittest.main()
