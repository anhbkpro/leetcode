import unittest
from typing import List
from .trapping_rain_water import Solution


class TestTrappingRainWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_height_array(self):
        """Test case with empty input array"""
        height = []
        self.assertEqual(self.solution.trap(height), 0)

    def test_single_element(self):
        """Test case with single element"""
        height = [5]
        self.assertEqual(self.solution.trap(height), 0)

    def test_no_trap(self):
        """Test case where no water can be trapped"""
        height = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.trap(height), 0)

        height = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.trap(height), 0)

    def test_simple_trap(self):
        """Test case with simple water trapping scenario"""
        height = [2, 0, 2]
        self.assertEqual(self.solution.trap(height), 2)

        height = [3, 0, 3]
        self.assertEqual(self.solution.trap(height), 3)

    def test_complex_trap(self):
        """Test case with multiple water trapping sections"""
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(self.solution.trap(height), 6)

    def test_decreasing_walls(self):
        """Test case with decreasing height walls"""
        height = [4, 2, 3]
        self.assertEqual(self.solution.trap(height), 1)

    def test_increasing_walls(self):
        """Test case with increasing height walls"""
        height = [2, 1, 3]
        self.assertEqual(self.solution.trap(height), 1)

    def test_plateau(self):
        """Test case with plateau-like structure"""
        height = [2, 0, 2, 2, 0, 2]
        self.assertEqual(self.solution.trap(height), 4)

    def test_large_values(self):
        """Test case with large height values"""
        height = [10000, 0, 10000]
        self.assertEqual(self.solution.trap(height), 10000)

    def test_leetcode_example(self):
        """Test the example from LeetCode"""
        height = [4, 2, 0, 3, 2, 5]
        self.assertEqual(self.solution.trap(height), 9)


if __name__ == "__main__":
    unittest.main()
