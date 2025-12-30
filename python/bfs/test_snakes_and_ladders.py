import unittest

from bfs.snakes_and_ladders import Solution


class TestSnakesAndLadders(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_small_board(self):
        board = [[-1, -1], [-1, -1]]
        self.assertEqual(self.solution.snakesAndLadders(board), 1)

    def test_no_snakes_or_ladders(self):
        board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.assertEqual(self.solution.snakesAndLadders(board), 2)

    def test_with_snakes(self):
        board = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
        board[3][0] = 1  # Snake from 13 to 1
        self.assertEqual(self.solution.snakesAndLadders(board), 3)

    def test_with_ladders(self):
        board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        board[2][0] = 8  # Ladder from 7 to 8
        self.assertEqual(self.solution.snakesAndLadders(board), 2)

    def test_complex_board(self):
        board = [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1],
        ]
        self.assertEqual(self.solution.snakesAndLadders(board), 4)

    def test_unreachable_board(self):
        board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        # Create a cycle: 1->2->3->1
        board[2][2] = 2  # Snake from 1 to 2
        board[2][1] = 3  # Snake from 2 to 3
        board[2][0] = 1  # Snake from 3 to 1
        self.assertEqual(self.solution.snakesAndLadders(board), 2)

    def test_multiple_paths(self):
        board = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
        board[3][0] = 8  # Ladder from 13 to 8
        board[2][0] = 8  # Ladder from 9 to 8
        self.assertEqual(self.solution.snakesAndLadders(board), 3)

    def test_edge_cases(self):
        # Test with minimum valid board size (2x2)
        board = [[-1, -1], [-1, -1]]
        self.assertEqual(self.solution.snakesAndLadders(board), 1)

        # Test with all ladders
        board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        board[2][0] = 8  # Ladder from 7 to 8
        board[1][0] = 8  # Ladder from 4 to 8
        board[0][0] = 8  # Ladder from 1 to 8
        self.assertEqual(self.solution.snakesAndLadders(board), 2)


if __name__ == "__main__":
    unittest.main()
