import unittest
from sliding_windows.max_consecutive_ones_ii import Solution


class TestMaxConsecutiveOnesII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        """Test with an empty array"""
        nums = []
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 0)

    def test_all_ones(self):
        """Test array with all ones"""
        nums = [1, 1, 1, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 5)

    def test_all_zeros(self):
        """Test array with all zeros"""
        nums = [0, 0, 0, 0, 0]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 1)

    def test_single_zero(self):
        """Test array with a single zero"""
        nums = [1, 1, 0, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 5)

    def test_two_zeros_separated(self):
        """Test array with two zeros separated by ones"""
        nums = [1, 0, 1, 1, 0, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 4)

    def test_consecutive_zeros(self):
        """Test array with consecutive zeros"""
        nums = [1, 1, 0, 0, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 3)

    def test_single_element_zero(self):
        """Test array with a single zero element"""
        nums = [0]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 1)

    def test_single_element_one(self):
        """Test array with a single one element"""
        nums = [1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 1)

    def test_alternating_ones_zeros(self):
        """Test array with alternating ones and zeros"""
        nums = [1, 0, 1, 0, 1, 0]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 3)

    def test_complex_sequence(self):
        """Test array with a more complex sequence"""
        nums = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 5)


if __name__ == "__main__":
    unittest.main()
