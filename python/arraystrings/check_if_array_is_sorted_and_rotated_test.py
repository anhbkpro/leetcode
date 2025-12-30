import unittest

from .check_if_array_is_sorted_and_rotated import Solution, SolutionFindSmallestElement


class TestCheckIfArrayIsSortedAndRotated(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sorted_array(self):
        """Test with already sorted array should return True"""
        nums = [1, 2, 3, 4, 5]
        self.assertTrue(self.solution.check(nums))

    def test_rotated_sorted_array(self):
        """Test with rotated sorted array should return True"""
        nums = [3, 4, 5, 1, 2]
        self.assertTrue(self.solution.check(nums))

    def test_unsorted_array(self):
        """Test with unsorted array should return False"""
        nums = [2, 1, 3, 4]
        self.assertFalse(self.solution.check(nums))

    def test_single_element_array(self):
        """Test with single element array should return True"""
        nums = [1]
        self.assertTrue(self.solution.check(nums))

    def test_empty_array(self):
        """Test with empty array should return True"""
        nums = []
        self.assertTrue(self.solution.check(nums))

    def test_duplicate_elements(self):
        """Test with array containing duplicate elements"""
        nums = [2, 1, 3, 2]
        self.assertFalse(self.solution.check(nums))

    def test_to_str_method(self):
        """Test the helper to_str method"""
        nums = [1, 2, 3]
        expected = "1-2-3"
        self.assertEqual(self.solution.to_str(nums), expected)


if __name__ == "__main__":
    unittest.main()
