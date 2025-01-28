import unittest
from hashing.make_lexicographically_smallest_array_by_swapping_elements import Solution


class TestLexicographicallySmallestArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case where elements can be swapped within limit to make array smaller."""
        nums = [1, 5, 3, 9, 8]
        limit = 2
        expected = [1, 3, 5, 8, 9]
        self.assertEqual(
            self.solution.lexicographicallySmallestArray(nums, limit), expected
        )

    def test_example_2(self):
        """Test case where no swaps are possible due to limit."""
        nums = [1, 7, 6, 18, 2, 1]
        limit = 3
        expected = [1, 6, 7, 18, 1, 2]  # Numbers within limit=3 can be swapped
        self.assertEqual(
            self.solution.lexicographicallySmallestArray(nums, limit), expected
        )

    def test_single_element(self):
        """Test array with a single element."""
        nums = [5]
        limit = 10
        expected = [5]
        self.assertEqual(
            self.solution.lexicographicallySmallestArray(nums, limit), expected
        )

    def test_all_same_elements(self):
        """Test array with all same elements."""
        nums = [3, 3, 3, 3]
        limit = 1
        expected = [3, 3, 3, 3]
        self.assertEqual(
            self.solution.lexicographicallySmallestArray(nums, limit), expected
        )

    def test_already_sorted(self):
        """Test array that is already sorted."""
        nums = [1, 2, 3, 4, 5]
        limit = 1
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(
            self.solution.lexicographicallySmallestArray(nums, limit), expected
        )

    def test_large_limit(self):
        """Test with limit larger than array range."""
        nums = [5, 2, 8, 1, 3]
        limit = 100
        expected = [1, 2, 3, 5, 8]
        self.assertEqual(
            self.solution.lexicographicallySmallestArray(nums, limit), expected
        )

    def test_zero_limit(self):
        """Test with zero limit, which should prevent any swaps."""
        nums = [3, 1, 2]
        limit = 0
        expected = [3, 1, 2]
        self.assertEqual(
            self.solution.lexicographicallySmallestArray(nums, limit), expected
        )

    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-3, 1, -1, 0, -2]
        limit = 2
        expected = [-3, -2, -1, 0, 1]
        self.assertEqual(
            self.solution.lexicographicallySmallestArray(nums, limit), expected
        )

    def test_multiple_groups(self):
        """Test case where numbers form multiple groups due to limit."""
        nums = [1, 12, 3, 14, 5, 16]
        limit = 2
        expected = [1, 12, 3, 14, 5, 16]
        self.assertEqual(
            self.solution.lexicographicallySmallestArray(nums, limit), expected
        )

    def test_duplicate_numbers(self):
        """Test with duplicate numbers within limit."""
        nums = [2, 4, 2, 4, 3]
        limit = 2
        expected = [2, 2, 3, 4, 4]
        self.assertEqual(
            self.solution.lexicographicallySmallestArray(nums, limit), expected
        )


if __name__ == "__main__":
    unittest.main()
