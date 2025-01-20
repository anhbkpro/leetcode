import unittest
from typing import List
from .first_completely_painted_row_or_column import Solution


class TestFirstCompleteIndex(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_element_matrix(self):
        """Test case with 1x1 matrix"""
        arr = [1]
        mat = [[1]]
        self.assertEqual(self.solution.firstCompleteIndex(arr, mat), 0)

    def test_single_row_matrix(self):
        """Test case with 1xN matrix"""
        arr = [3, 2, 1]
        mat = [[1, 2, 3]]
        self.assertEqual(self.solution.firstCompleteIndex(arr, mat), 0)

    def test_single_column_matrix(self):
        """Test case with Mx1 matrix"""
        arr = [3, 2, 1]
        mat = [[1], [2], [3]]
        self.assertEqual(self.solution.firstCompleteIndex(arr, mat), 0)

    def test_complete_row_first(self):
        """Test case where a row completes before any column"""
        arr = [1, 2, 3, 4, 5, 6]
        mat = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(self.solution.firstCompleteIndex(arr, mat), 2)

    def test_complete_column_first(self):
        """Test case where a column completes before any row"""
        arr = [1, 4, 2, 5, 3, 6]
        mat = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(self.solution.firstCompleteIndex(arr, mat), 1)

    def test_leetcode_example1(self):
        """Test the first example from LeetCode"""
        arr = [1, 3, 4, 2]
        mat = [[1, 4], [2, 3]]
        self.assertEqual(self.solution.firstCompleteIndex(arr, mat), 2)

    def test_leetcode_example2(self):
        """Test the second example from LeetCode"""
        arr = [2, 8, 7, 4, 1, 3, 5, 6, 9]
        mat = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
        self.assertEqual(self.solution.firstCompleteIndex(arr, mat), 3)

    def test_square_matrix(self):
        """Test case with square matrix where all numbers are unique"""
        arr = [5, 4, 3, 1, 2, 6, 7, 8, 9]
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.solution.firstCompleteIndex(arr, mat), 4)

    def test_rectangular_matrix(self):
        """Test case with rectangular matrix"""
        arr = [1, 4, 7, 2, 5, 8, 3, 6, 9, 10, 11, 12]
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertEqual(self.solution.firstCompleteIndex(arr, mat), 6)

    def test_last_element_completion(self):
        """Test case where completion happens at the last element"""
        arr = [2, 3, 4, 1]
        mat = [[1, 2], [3, 4]]
        self.assertEqual(self.solution.firstCompleteIndex(arr, mat), 2)

    def test_large_numbers(self):
        """Test case with large numbers in matrix"""
        arr = [1000000, 999999, 999998]
        mat = [[999998, 999999, 1000000]]
        self.assertEqual(self.solution.firstCompleteIndex(arr, mat), 0)


if __name__ == "__main__":
    unittest.main()
