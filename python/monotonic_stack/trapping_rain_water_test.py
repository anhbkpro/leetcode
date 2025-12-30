import pytest

from .trapping_rain_water import BruteForce, DynamicProgramming, Stack, TwoPointers


@pytest.mark.parametrize(
    "solution", [BruteForce(), DynamicProgramming(), Stack(), TwoPointers()]
)
class TestTrappingRainWater:
    def test_empty_height_array(self, solution):
        """Test case with empty input array"""
        assert solution.trap([]) == 0

    def test_single_element(self, solution):
        """Test case with single element"""
        assert solution.trap([5]) == 0

    def test_no_trap(self, solution):
        """Test case where no water can be trapped"""
        assert solution.trap([1, 2, 3, 4, 5]) == 0
        assert solution.trap([5, 4, 3, 2, 1]) == 0

    def test_simple_trap(self, solution):
        """Test case with simple water trapping scenario"""
        assert solution.trap([2, 0, 2]) == 2
        assert solution.trap([3, 0, 3]) == 3

    def test_complex_trap(self, solution):
        """Test case with multiple water trapping sections"""
        assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    def test_decreasing_walls(self, solution):
        """Test case with decreasing height walls"""
        assert solution.trap([4, 2, 3]) == 1

    def test_increasing_walls(self, solution):
        """Test case with increasing height walls"""
        assert solution.trap([2, 1, 3]) == 1

    def test_plateau(self, solution):
        """Test case with plateau-like structure"""
        assert solution.trap([2, 0, 2, 2, 0, 2]) == 4

    def test_large_values(self, solution):
        """Test case with large height values"""
        assert solution.trap([10000, 0, 10000]) == 10000

    def test_leetcode_example(self, solution):
        """Test the example from LeetCode"""
        assert solution.trap([4, 2, 0, 3, 2, 5]) == 9

    def test_all_zeros(self, solution):
        """Test case with all zero heights"""
        assert solution.trap([0, 0, 0, 0]) == 0

    def test_alternating_heights(self, solution):
        """Test case with alternating heights"""
        assert solution.trap([1, 0, 1, 0, 1, 0, 1]) == 3

    def test_equal_heights(self, solution):
        """Test case with equal heights"""
        assert solution.trap([2, 2, 2, 2]) == 0

    def test_symmetric_heights(self, solution):
        """Test case with symmetric height pattern"""
        assert solution.trap([1, 2, 3, 2, 1]) == 0
