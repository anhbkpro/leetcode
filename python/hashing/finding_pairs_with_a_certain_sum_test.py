import unittest
from typing import List

from .finding_pairs_with_a_certain_sum import FindSumPairs


class TestFindSumPairs(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        pass

    def test_initialization(self):
        """Test the constructor initializes correctly"""
        nums1 = [1, 1, 2, 2, 2, 3]
        nums2 = [1, 4, 5, 2, 5, 4]

        find_sum_pairs = FindSumPairs(nums1, nums2)

        self.assertEqual(find_sum_pairs.nums1, nums1)
        self.assertEqual(find_sum_pairs.nums2, nums2)
        # Check that the counter is properly initialized
        expected_counter = {1: 1, 4: 2, 5: 2, 2: 1}
        self.assertEqual(dict(find_sum_pairs.cnt), expected_counter)

    def test_add_operation(self):
        """Test the add operation updates nums2 and counter correctly"""
        nums1 = [1, 1, 2, 2, 2, 3]
        nums2 = [1, 4, 5, 2, 5, 4]

        find_sum_pairs = FindSumPairs(nums1, nums2)

        # Add 3 to index 1 (value 4 becomes 7)
        find_sum_pairs.add(1, 3)

        # Check nums2 is updated
        expected_nums2 = [1, 7, 5, 2, 5, 4]
        self.assertEqual(find_sum_pairs.nums2, expected_nums2)

        # Check counter is updated
        expected_counter = {1: 1, 7: 1, 5: 2, 2: 1, 4: 1}
        self.assertEqual(dict(find_sum_pairs.cnt), expected_counter)

    def test_add_operation_multiple_times(self):
        """Test multiple add operations"""
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3]

        find_sum_pairs = FindSumPairs(nums1, nums2)

        # Add 5 to index 0
        find_sum_pairs.add(0, 5)
        self.assertEqual(find_sum_pairs.nums2[0], 6)

        # Add 10 to index 1
        find_sum_pairs.add(1, 10)
        self.assertEqual(find_sum_pairs.nums2[1], 12)

        # Add -2 to index 2
        find_sum_pairs.add(2, -2)
        self.assertEqual(find_sum_pairs.nums2[2], 1)

        # Check final counter
        expected_counter = {1: 1, 2: 0, 3: 0, 6: 1, 12: 1}
        self.assertEqual(dict(find_sum_pairs.cnt), expected_counter)

    def test_count_operation_basic(self):
        """Test basic count operation"""
        nums1 = [1, 1, 2, 2, 2, 3]
        nums2 = [1, 4, 5, 2, 5, 4]

        find_sum_pairs = FindSumPairs(nums1, nums2)

        # Count pairs that sum to 7
        # nums1: [1, 1, 2, 2, 2, 3]
        # nums2: [1, 4, 5, 2, 5, 4]
        # For target 7:
        # 1 + 6 (not in nums2) = 0 pairs
        # 2 + 5 (5 appears twice) = 2 * 3 = 6 pairs
        # 3 + 4 (4 appears twice) = 1 * 2 = 2 pairs
        # Total: 8 pairs
        result = find_sum_pairs.count(7)
        self.assertEqual(result, 8)

    def test_count_operation_no_pairs(self):
        """Test count operation when no pairs exist"""
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3]

        find_sum_pairs = FindSumPairs(nums1, nums2)

        # Count pairs that sum to 100 (impossible)
        result = find_sum_pairs.count(100)
        self.assertEqual(result, 0)

    def test_count_operation_all_pairs(self):
        """Test count operation when all elements can form pairs"""
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3]

        find_sum_pairs = FindSumPairs(nums1, nums2)

        # Count pairs that sum to 4
        # 1 + 3 = 4 (3 appears once) = 1 pair
        # 2 + 2 = 4 (2 appears once) = 1 pair
        # 3 + 1 = 4 (1 appears once) = 1 pair
        # Total: 3 pairs
        result = find_sum_pairs.count(4)
        self.assertEqual(result, 3)

    def test_add_and_count_sequence(self):
        """Test a sequence of add and count operations"""
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3]

        find_sum_pairs = FindSumPairs(nums1, nums2)

        # Initial count for target 4
        result1 = find_sum_pairs.count(4)
        self.assertEqual(result1, 3)

        # Add 1 to index 0 (1 becomes 2)
        find_sum_pairs.add(0, 1)

        # Count for target 4 after modification
        # nums1: [1, 2, 3]
        # nums2: [2, 2, 3] (after adding 1 to index 0)
        # 1 + 3 = 4 (3 appears once) = 1 pair
        # 2 + 2 = 4 (2 appears twice) = 2 pairs
        # 3 + 1 = 4 (1 doesn't exist) = 0 pairs
        # Total: 3 pairs
        result2 = find_sum_pairs.count(4)
        self.assertEqual(result2, 3)

        # Add 5 to index 2 (3 becomes 8)
        find_sum_pairs.add(2, 5)

        # Count for target 4 after second modification
        # nums1: [1, 2, 3]
        # nums2: [2, 2, 8] (after adding 5 to index 2)
        # 1 + 3 = 4 (3 doesn't exist) = 0 pairs
        # 2 + 2 = 4 (2 appears twice) = 2 pairs
        # 3 + 1 = 4 (1 doesn't exist) = 0 pairs
        # Total: 2 pairs
        result3 = find_sum_pairs.count(4)
        self.assertEqual(result3, 2)

    def test_edge_cases(self):
        """Test edge cases"""
        # Empty arrays
        find_sum_pairs = FindSumPairs([], [])
        self.assertEqual(find_sum_pairs.count(5), 0)

        # Single element arrays
        find_sum_pairs = FindSumPairs([1], [2])
        self.assertEqual(find_sum_pairs.count(3), 1)
        self.assertEqual(find_sum_pairs.count(5), 0)

        # Arrays with negative numbers
        nums1 = [-1, -2, -3]
        nums2 = [-1, -2, -3]
        find_sum_pairs = FindSumPairs(nums1, nums2)

        # Count pairs that sum to -4
        # -1 + -3 = -4 (3 appears once) = 1 pair
        # -2 + -2 = -4 (2 appears once) = 1 pair
        # -3 + -1 = -4 (1 appears once) = 1 pair
        # Total: 3 pairs
        result = find_sum_pairs.count(-4)
        self.assertEqual(result, 3)

    def test_duplicate_elements(self):
        """Test with duplicate elements in both arrays"""
        nums1 = [1, 1, 1, 2, 2]
        nums2 = [1, 1, 2, 2, 2]

        find_sum_pairs = FindSumPairs(nums1, nums2)

        # Count pairs that sum to 3
        # 1 + 2 = 3 (1 appears 3 times, 2 appears 3 times) = 3 * 3 = 9 pairs
        # 2 + 1 = 3 (2 appears 2 times, 1 appears 2 times) = 2 * 2 = 4 pairs
        # Total: 13 pairs
        result = find_sum_pairs.count(3)
        self.assertEqual(result, 13)

    def test_large_numbers(self):
        """Test with large numbers"""
        nums1 = [1000000, 2000000, 3000000]
        nums2 = [1000000, 2000000, 3000000]

        find_sum_pairs = FindSumPairs(nums1, nums2)

        # Count pairs that sum to 4000000
        # 1000000 + 3000000 = 4000000 (3000000 appears once) = 1 pair
        # 2000000 + 2000000 = 4000000 (2000000 appears once) = 1 pair
        # 3000000 + 1000000 = 4000000 (1000000 appears once) = 1 pair
        # Total: 3 pairs
        result = find_sum_pairs.count(4000000)
        self.assertEqual(result, 3)

    def test_zero_values(self):
        """Test with zero values"""
        nums1 = [0, 1, 2, 0]
        nums2 = [0, 1, 2, 0]

        find_sum_pairs = FindSumPairs(nums1, nums2)

        # Count pairs that sum to 0
        # 0 + 0 = 0 (0 appears twice in nums2) = 2 * 2 = 4 pairs
        # 1 + -1 = 0 (-1 doesn't exist) = 0 pairs
        # 2 + -2 = 0 (-2 doesn't exist) = 0 pairs
        # Total: 4 pairs
        result = find_sum_pairs.count(0)
        self.assertEqual(result, 4)

    def test_add_operation_edge_cases(self):
        """Test add operation with edge cases"""
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3]

        find_sum_pairs = FindSumPairs(nums1, nums2)

        # Add 0 (no change)
        find_sum_pairs.add(0, 0)
        self.assertEqual(find_sum_pairs.nums2[0], 1)

        # Add negative number
        find_sum_pairs.add(1, -5)
        self.assertEqual(find_sum_pairs.nums2[1], -3)

        # Add large number
        find_sum_pairs.add(2, 1000000)
        self.assertEqual(find_sum_pairs.nums2[2], 1000003)


if __name__ == "__main__":
    unittest.main()
