import unittest
from .bitwise_xor_of_all_pairings import Solution


class TestXORAllNums(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example case from the problem statement"""
        nums1 = [2, 1, 3]
        nums2 = [10, 2, 5, 0]
        expected = 13
        result = self.solution.xorAllNums(nums1, nums2)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """Test the second example case from the problem statement"""
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected = 0
        result = self.solution.xorAllNums(nums1, nums2)
        self.assertEqual(result, expected)

    def test_single_element_arrays(self):
        """Test when both arrays have single elements"""
        nums1 = [5]
        nums2 = [7]
        expected = 5 ^ 7  # Direct XOR of the only possible pair
        result = self.solution.xorAllNums(nums1, nums2)
        self.assertEqual(result, expected)

    def test_same_numbers_in_both_arrays(self):
        """Test when both arrays contain same numbers"""
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3]
        result = self.solution.xorAllNums(nums1, nums2)
        # Each number appears in both arrays, so their frequencies matter
        self.assertEqual(result, 0)

    def test_zero_elements(self):
        """Test when arrays contain zero"""
        nums1 = [0, 1]
        nums2 = [0]
        result = self.solution.xorAllNums(nums1, nums2)
        # Verify XOR with zero doesn't change the result
        self.assertEqual(result, 1)

    def test_large_numbers(self):
        """Test with numbers close to the constraint limit"""
        nums1 = [10**9]
        nums2 = [10**9 - 1]
        expected = 10**9 ^ (10**9 - 1)
        result = self.solution.xorAllNums(nums1, nums2)
        self.assertEqual(result, expected)

    def test_power_of_two(self):
        """Test with powers of 2 which have special properties in XOR operations"""
        nums1 = [2, 4, 8]
        nums2 = [16, 32]
        result = self.solution.xorAllNums(nums1, nums2)
        # Manually calculate expected result
        expected = 0
        for x in nums1:
            for y in nums2:
                expected ^= x ^ y
        self.assertEqual(result, expected)

    def test_repeated_numbers(self):
        """Test with repeated numbers in the arrays"""
        nums1 = [1, 1, 1]
        nums2 = [2, 2]
        result = self.solution.xorAllNums(nums1, nums2)
        # Each 1 appears twice (paired with each 2)
        # Each 2 appears three times (paired with each 1)
        expected = 0  # All numbers appear even times
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
