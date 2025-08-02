import unittest
from arraystrings.pascals_triangle import Solution


class TestPascalsTriangle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_zero_rows(self):
        """Test with zero rows (edge case)"""
        numRows = 0
        expected = []
        result = self.solution.generate(numRows)
        self.assertEqual(result, expected)

    def test_one_row(self):
        """Test with one row"""
        numRows = 1
        expected = [[1]]
        result = self.solution.generate(numRows)
        self.assertEqual(result, expected)

    def test_two_rows(self):
        """Test with two rows"""
        numRows = 2
        expected = [[1], [1, 1]]
        result = self.solution.generate(numRows)
        self.assertEqual(result, expected)

    def test_three_rows(self):
        """Test with three rows"""
        numRows = 3
        expected = [[1], [1, 1], [1, 2, 1]]
        result = self.solution.generate(numRows)
        self.assertEqual(result, expected)

    def test_four_rows(self):
        """Test with four rows"""
        numRows = 4
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        result = self.solution.generate(numRows)
        self.assertEqual(result, expected)

    def test_five_rows(self):
        """Test with five rows"""
        numRows = 5
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        result = self.solution.generate(numRows)
        self.assertEqual(result, expected)

    def test_six_rows(self):
        """Test with six rows"""
        numRows = 6
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
        ]
        result = self.solution.generate(numRows)
        self.assertEqual(result, expected)

    def test_seven_rows(self):
        """Test with seven rows"""
        numRows = 7
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
        ]
        result = self.solution.generate(numRows)
        self.assertEqual(result, expected)

    def test_negative_rows(self):
        """Test with negative number of rows (edge case)"""
        numRows = -1
        expected = []
        result = self.solution.generate(numRows)
        self.assertEqual(result, expected)

    def test_large_number_of_rows(self):
        """Test with a larger number of rows"""
        numRows = 10
        result = self.solution.generate(numRows)

        # Check that we have the correct number of rows
        self.assertEqual(len(result), numRows)

        # Check that each row has the correct length
        for i, row in enumerate(result):
            self.assertEqual(len(row), i + 1)

        # Check that first and last elements of each row are 1
        for row in result:
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)

        # Check that the triangle follows Pascal's rule
        for i in range(2, len(result)):
            for j in range(1, len(result[i]) - 1):
                expected = result[i - 1][j - 1] + result[i - 1][j]
                self.assertEqual(result[i][j], expected)

    def test_pascals_triangle_properties(self):
        """Test that the generated triangle follows Pascal's triangle properties"""
        numRows = 8
        result = self.solution.generate(numRows)

        # Property 1: Each row has n+1 elements where n is the row number (0-indexed)
        for i, row in enumerate(result):
            self.assertEqual(len(row), i + 1)

        # Property 2: First and last elements of each row are 1
        for row in result:
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)

        # Property 3: Each element (except first and last) is sum of two elements above it
        for i in range(2, len(result)):
            for j in range(1, len(result[i]) - 1):
                expected = result[i - 1][j - 1] + result[i - 1][j]
                self.assertEqual(result[i][j], expected)

    def test_row_sums(self):
        """Test that sum of elements in each row equals 2^n where n is row number (0-indexed)"""
        numRows = 6
        result = self.solution.generate(numRows)

        for i, row in enumerate(result):
            expected_sum = 2**i
            actual_sum = sum(row)
            self.assertEqual(actual_sum, expected_sum)

    def test_symmetry(self):
        """Test that each row is symmetric (palindrome)"""
        numRows = 7
        result = self.solution.generate(numRows)

        for row in result:
            # Check if row is symmetric
            self.assertEqual(row, row[::-1])

    def test_empty_result_structure(self):
        """Test that empty result has correct structure"""
        numRows = 0
        result = self.solution.generate(numRows)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_single_row_structure(self):
        """Test that single row has correct structure"""
        numRows = 1
        result = self.solution.generate(numRows)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 1)
        self.assertEqual(result[0][0], 1)

    def test_two_rows_structure(self):
        """Test that two rows have correct structure"""
        numRows = 2
        result = self.solution.generate(numRows)
        self.assertEqual(len(result), 2)
        self.assertEqual(len(result[0]), 1)
        self.assertEqual(len(result[1]), 2)
        self.assertEqual(result[0], [1])
        self.assertEqual(result[1], [1, 1])

    def test_three_rows_structure(self):
        """Test that three rows have correct structure"""
        numRows = 3
        result = self.solution.generate(numRows)
        self.assertEqual(len(result), 3)
        self.assertEqual(len(result[0]), 1)
        self.assertEqual(len(result[1]), 2)
        self.assertEqual(len(result[2]), 3)
        self.assertEqual(result[0], [1])
        self.assertEqual(result[1], [1, 1])
        self.assertEqual(result[2], [1, 2, 1])


if __name__ == "__main__":
    unittest.main()
