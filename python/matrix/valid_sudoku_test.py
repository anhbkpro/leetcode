import unittest
from typing import List

from matrix.valid_sudoku import Solution


class TestValidSudoku(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_sudoku(self):
        """Test a valid Sudoku board"""
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        expected = True
        result = self.solution.isValidSudoku(board)
        self.assertEqual(result, expected)

    def test_invalid_sudoku_duplicate_in_row(self):
        """Test invalid Sudoku with duplicate in row"""
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        expected = False
        result = self.solution.isValidSudoku(board)
        self.assertEqual(result, expected)

    def test_invalid_sudoku_duplicate_in_column(self):
        """Test invalid Sudoku with duplicate in column"""
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            ["5", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        expected = False
        result = self.solution.isValidSudoku(board)
        self.assertEqual(result, expected)

    def test_invalid_sudoku_duplicate_in_box(self):
        """Test invalid Sudoku with duplicate in 3x3 box"""
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        # Modify to have duplicate in first 3x3 box
        board[0][0] = "9"  # This creates a duplicate with board[1][4] = "9"
        expected = False
        result = self.solution.isValidSudoku(board)
        self.assertEqual(result, expected)

    def test_empty_board(self):
        """Test board with all empty cells"""
        board = [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected = True
        result = self.solution.isValidSudoku(board)
        self.assertEqual(result, expected)

    def test_partially_filled_valid_board(self):
        """Test partially filled valid board"""
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        expected = True
        result = self.solution.isValidSudoku(board)
        self.assertEqual(result, expected)

    def test_completed_valid_sudoku(self):
        """Test a completed valid Sudoku board"""
        board = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ]
        expected = True
        result = self.solution.isValidSudoku(board)
        self.assertEqual(result, expected)

    def test_invalid_sudoku_multiple_violations(self):
        """Test invalid Sudoku with multiple rule violations"""
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            ["8", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        expected = False
        result = self.solution.isValidSudoku(board)
        self.assertEqual(result, expected)

    def test_single_number_board(self):
        """Test board with only one number"""
        board = [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "5", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected = True
        result = self.solution.isValidSudoku(board)
        self.assertEqual(result, expected)

    def test_invalid_sudoku_same_number_in_same_box(self):
        """Test invalid Sudoku with same number in same 3x3 box"""
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        # Add a duplicate in the first 3x3 box (positions [0,0] and [1,1])
        board[1][1] = "5"  # This creates a duplicate with board[0][0] = "5"
        expected = False
        result = self.solution.isValidSudoku(board)
        self.assertEqual(result, expected)

    def test_edge_case_all_same_number_in_different_positions(self):
        """Test edge case with all same numbers in valid positions"""
        board = [
            ["1", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "1", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "1", ".", "."],
            [".", "1", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "1", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "1", "."],
            [".", ".", "1", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "1", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "1"],
        ]
        expected = True
        result = self.solution.isValidSudoku(board)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
