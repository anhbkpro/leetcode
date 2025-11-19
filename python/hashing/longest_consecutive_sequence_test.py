import unittest
from .longest_consecutive_sequence import Solution


class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test example case from problem statement"""
        nums = [100, 4, 200, 1, 3, 2]
        self.assertEqual(self.solution.longestConsecutive(nums), 4)

    def test_example_2(self):
        """Test example case from problem statement"""
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        self.assertEqual(self.solution.longestConsecutive(nums), 9)

    def test_empty_array(self):
        """Test with empty array"""
        nums = []
        self.assertEqual(self.solution.longestConsecutive(nums), 0)

    def test_single_element(self):
        """Test with single element"""
        nums = [1]
        self.assertEqual(self.solution.longestConsecutive(nums), 1)

    def test_duplicate_elements(self):
        """Test with duplicate elements"""
        nums = [1, 2, 0, 1]
        self.assertEqual(self.solution.longestConsecutive(nums), 3)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-5, -4, -3, -2, 0, 1]
        self.assertEqual(self.solution.longestConsecutive(nums), 4)

    def test_all_duplicates(self):
        """Test when all elements are duplicates"""
        nums = [1, 1, 1, 1]
        self.assertEqual(self.solution.longestConsecutive(nums), 1)

    def test_multiple_sequences(self):
        """Test with multiple consecutive sequences"""
        nums = [1, 2, 3, 10, 11, 12, 13, 14]
        self.assertEqual(self.solution.longestConsecutive(nums), 5)

    def test_scattered_sequence(self):
        """Test with scattered elements that form a sequence"""
        nums = [4, 1, 3, 2]
        self.assertEqual(self.solution.longestConsecutive(nums), 4)

    def test_large_gaps(self):
        """Test with large gaps between numbers"""
        nums = [1, 1000000, 2, 1000001, 1000002]
        self.assertEqual(self.solution.longestConsecutive(nums), 3)

    def test_alternating_sequence(self):
        """Test with alternating sequence pattern"""
        nums = [1, 3, 2, 4, 6, 5]
        self.assertEqual(self.solution.longestConsecutive(nums), 6)


if __name__ == "__main__":
    unittest.main()
