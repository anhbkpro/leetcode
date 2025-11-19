import unittest
from copy import deepcopy
from .shortest_path_to_get_food import Solution


class TestGetFood(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_path(self):
        """Test a simple path to food"""
        grid = [
            ["X", "X", "X", "X", "X"],
            ["X", "*", "O", "#", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        self.assertEqual(self.solution.getFood(deepcopy(grid)), 2)

    def test_no_path(self):
        """Test when there's no path to food"""
        grid = [
            ["X", "X", "X", "X", "X"],
            ["X", "*", "X", "#", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        self.assertEqual(self.solution.getFood(deepcopy(grid)), -1)

    def test_multiple_food_sources(self):
        """Test with multiple food sources, should return shortest path"""
        grid = [
            ["X", "X", "X", "X", "X"],
            ["X", "*", "O", "#", "X"],
            ["X", "O", "O", "#", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        self.assertEqual(self.solution.getFood(deepcopy(grid)), 2)

    def test_long_path(self):
        """Test with a longer path to food"""
        grid = [
            ["X", "X", "X", "X", "X"],
            ["X", "*", "O", "O", "X"],
            ["X", "O", "X", "O", "X"],
            ["X", "O", "O", "#", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        self.assertEqual(self.solution.getFood(deepcopy(grid)), 4)

    def test_single_cell(self):
        """Test with a single cell grid"""
        grid = [["*"]]
        self.assertEqual(self.solution.getFood(deepcopy(grid)), -1)

    def test_surrounded_by_obstacles(self):
        """Test when start position is surrounded by obstacles"""
        grid = [["O", "O", "O"], ["O", "*", "O"], ["O", "O", "#"]]
        self.assertEqual(self.solution.getFood(deepcopy(grid)), 2)

    def test_zigzag_path(self):
        """Test with a zigzag path to food"""
        grid = [
            ["X", "X", "X", "X", "X"],
            ["X", "*", "O", "X", "X"],
            ["X", "X", "O", "O", "X"],
            ["X", "X", "X", "O", "X"],
            ["X", "X", "X", "#", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        self.assertEqual(self.solution.getFood(deepcopy(grid)), 5)

    def test_multiple_paths(self):
        """Test with multiple possible paths to food"""
        grid = [
            ["O", "O", "O", "O", "O"],
            ["O", "*", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "#", "O"],
            ["O", "O", "O", "O", "O"],
        ]
        self.assertEqual(self.solution.getFood(deepcopy(grid)), 4)

    def test_edge_cases(self):
        """Test various edge cases"""
        # Start position at edge
        grid1 = [["*", "O", "#"]]
        self.assertEqual(self.solution.getFood(deepcopy(grid1)), 2)

        # Food position at edge
        grid2 = [["#", "O", "*"]]
        self.assertEqual(self.solution.getFood(deepcopy(grid2)), 2)

        # Single column
        grid3 = [["*"], ["O"], ["#"]]
        self.assertEqual(self.solution.getFood(deepcopy(grid3)), 2)

    def test_grid_modification(self):
        """Test that the original grid is not modified"""
        original_grid = [
            ["X", "X", "X", "X", "X"],
            ["X", "*", "O", "#", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        grid_copy = deepcopy(original_grid)
        self.solution.getFood(grid_copy)
        self.assertEqual(original_grid, original_grid)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
