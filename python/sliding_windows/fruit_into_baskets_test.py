import unittest
from typing import List

from sliding_windows.fruit_into_baskets import Solution


class TestFruitIntoBaskets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case from LeetCode example 1"""
        fruits = [1, 2, 1]
        expected = 3
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """Test case from LeetCode example 2"""
        fruits = [0, 1, 2, 2]
        expected = 3
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_example_3(self):
        """Test case from LeetCode example 3"""
        fruits = [1, 2, 3, 2, 2]
        expected = 4
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_single_fruit_type(self):
        """Test with only one type of fruit"""
        fruits = [1, 1, 1, 1, 1]
        expected = 5
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_two_fruit_types(self):
        """Test with exactly two types of fruit"""
        fruits = [1, 2, 1, 2, 1, 2]
        expected = 6
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_three_fruit_types(self):
        """Test with three types of fruit - should limit to 2"""
        fruits = [1, 2, 3, 1, 2, 3]
        expected = 2
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_empty_array(self):
        """Test with empty array"""
        fruits = []
        expected = 0
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_single_element(self):
        """Test with single element"""
        fruits = [1]
        expected = 1
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_two_elements_different(self):
        """Test with two different elements"""
        fruits = [1, 2]
        expected = 2
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_two_elements_same(self):
        """Test with two same elements"""
        fruits = [1, 1]
        expected = 2
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_complex_pattern(self):
        """Test with complex pattern of fruits"""
        fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
        expected = 5
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_alternating_pattern(self):
        """Test with alternating pattern"""
        fruits = [1, 2, 1, 2, 1, 2, 1, 2]
        expected = 8
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_long_sequence_same_fruit(self):
        """Test with long sequence of same fruit followed by different"""
        fruits = [1, 1, 1, 1, 1, 1, 1, 1, 2, 3]
        expected = 9
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_maximum_window_at_end(self):
        """Test where maximum window is at the end"""
        fruits = [1, 2, 3, 4, 5, 1, 1, 1, 1]
        expected = 5
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_maximum_window_at_beginning(self):
        """Test where maximum window is at the beginning"""
        fruits = [1, 1, 1, 1, 2, 3, 4, 5]
        expected = 5
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_maximum_window_in_middle(self):
        """Test where maximum window is in the middle"""
        fruits = [1, 2, 3, 1, 1, 1, 2, 2, 2, 3, 4]
        expected = 6
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_all_different_fruits(self):
        """Test with all different fruits"""
        fruits = [1, 2, 3, 4, 5]
        expected = 2
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_zero_values(self):
        """Test with zero values"""
        fruits = [0, 0, 1, 1, 0, 0]
        expected = 6
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        """Test with large numbers"""
        fruits = [100, 200, 100, 200, 300, 100, 100]
        expected = 4
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        fruits = [-1, -2, -1, -2, -3, -1, -1]
        expected = 4
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        fruits = [1, -1, 1, -1, 2, 1, 1]
        expected = 4
        result = self.solution.totalFruit(fruits)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
