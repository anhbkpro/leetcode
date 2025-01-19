import unittest
import heapq
from typing import List
from .trapping_rain_water_ii import Solution


class TestTrappingRainWater3D(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_row(self):
        """Test case with single row height map"""
        height_map = [[1, 2, 3, 4, 5]]
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

    def test_single_column(self):
        """Test case with single column height map"""
        height_map = [[1], [2], [3], [4], [5]]
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

    def test_flat_surface(self):
        """Test case with flat surface where no water can be trapped"""
        height_map = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

    def test_simple_basin(self):
        """Test case with simple basin where water can be trapped"""
        height_map = [[3, 3, 3], [3, 1, 3], [3, 3, 3]]
        self.assertEqual(self.solution.trapRainWater(height_map), 2)

    def test_multiple_basins(self):
        """Test case with multiple basins"""
        height_map = [[3, 3, 3, 3], [3, 1, 2, 3], [3, 2, 1, 3], [3, 3, 3, 3]]
        self.assertEqual(self.solution.trapRainWater(height_map), 6)

    def test_uneven_walls(self):
        """Test case with uneven wall heights"""
        height_map = [[5, 5, 5], [5, 1, 5], [5, 2, 5], [5, 1, 5], [5, 5, 5]]
        self.assertEqual(self.solution.trapRainWater(height_map), 11)

    def test_leetcode_example1(self):
        """Test the first example from LeetCode"""
        height_map = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
        self.assertEqual(self.solution.trapRainWater(height_map), 4)

    def test_leetcode_example2(self):
        """Test the second example from LeetCode"""
        height_map = [
            [3, 3, 3, 3, 3],
            [3, 2, 2, 2, 3],
            [3, 2, 1, 2, 3],
            [3, 2, 2, 2, 3],
            [3, 3, 3, 3, 3],
        ]
        self.assertEqual(self.solution.trapRainWater(height_map), 10)

    def test_no_walls(self):
        """Test case where water cannot be trapped due to no walls"""
        height_map = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

    def test_large_values(self):
        """Test case with large height values"""
        height_map = [[10000, 10000, 10000], [10000, 0, 10000], [10000, 10000, 10000]]
        self.assertEqual(self.solution.trapRainWater(height_map), 10000)

    def test_is_valid_cell(self):
        """Test the helper method for cell validation"""
        self.assertTrue(self.solution._is_valid_cell(0, 0, 3, 3))
        self.assertTrue(self.solution._is_valid_cell(2, 2, 3, 3))
        self.assertFalse(self.solution._is_valid_cell(-1, 0, 3, 3))
        self.assertFalse(self.solution._is_valid_cell(0, -1, 3, 3))
        self.assertFalse(self.solution._is_valid_cell(3, 0, 3, 3))
        self.assertFalse(self.solution._is_valid_cell(0, 3, 3, 3))

    def test_cell_comparison(self):
        """Test the Cell class comparison method"""
        cell1 = self.solution.Cell(1, 0, 0)
        cell2 = self.solution.Cell(2, 0, 0)
        self.assertTrue(cell1 < cell2)
        self.assertFalse(cell2 < cell1)


if __name__ == "__main__":
    unittest.main()
