import unittest
from heaps.find_k_pairs_with_smallest_sums import Solution


class TestFindKPairsWithSmallestSums(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Test case from LeetCode example 1
        nums1 = [1, 7, 11]
        nums2 = [2, 4, 6]
        k = 3
        expected = [[1, 2], [1, 4], [1, 6]]
        result = self.solution.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(result, expected)

    def test_example_2(self):
        # Test case from LeetCode example 2
        nums1 = [1, 1, 2]
        nums2 = [1, 2, 3]
        k = 2
        expected = [[1, 1], [1, 1]]
        result = self.solution.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(result, expected)

    def test_example_3(self):
        # Test case from LeetCode example 3
        nums1 = [1, 2]
        nums2 = [3]
        k = 3
        expected = [[1, 3], [2, 3]]
        result = self.solution.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(result, expected)

    def test_k_larger_than_possible_pairs(self):
        # Test when k is larger than the number of possible pairs
        nums1 = [1]
        nums2 = [2, 3]
        k = 5
        expected = [[1, 2], [1, 3]]
        result = self.solution.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(result, expected)

    def test_single_elements(self):
        # Test with single elements in both arrays
        nums1 = [1]
        nums2 = [2]
        k = 1
        expected = [[1, 2]]
        result = self.solution.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(result, expected)

    def test_same_elements(self):
        # Test with arrays containing same elements
        nums1 = [1, 1, 1]
        nums2 = [1, 1, 1]
        k = 4
        expected = [[1, 1], [1, 1], [1, 1], [1, 1]]
        result = self.solution.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
