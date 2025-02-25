import unittest
from dp.number_of_sub_arrays_with_odd_sum import Solution


class TestNumberOfSubarraysWithOddSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_even_number(self):
        """Test with a single even number"""
        arr = [2]
        self.assertEqual(self.solution.numOfSubarrays(arr), 0)

    def test_single_odd_number(self):
        """Test with a single odd number"""
        arr = [1]
        self.assertEqual(self.solution.numOfSubarrays(arr), 1)

    def test_all_even_numbers(self):
        """Test with all even numbers"""
        arr = [2, 4, 6, 8]
        self.assertEqual(self.solution.numOfSubarrays(arr), 0)

    def test_all_odd_numbers(self):
        """Test with all odd numbers"""
        arr = [1, 3, 5]
        # Subarrays with odd sum: [1], [3], [5], [1,3,5]
        self.assertEqual(self.solution.numOfSubarrays(arr), 4)

    def test_mixed_numbers(self):
        """Test with mixed odd and even numbers"""
        arr = [1, 2, 3, 4, 5]
        # Subarrays with odd sum: [1], [3], [5], [1,2], [2,3], [4,5], [1,2,3], [3,4,5], [1,2,3,4,5]
        self.assertEqual(self.solution.numOfSubarrays(arr), 9)

    def test_large_numbers(self):
        """Test with large numbers"""
        arr = [100, 101, 102, 103]
        # After modulo 2: [0, 1, 0, 1]
        # Subarrays with odd sum: [101], [103], [100,101], [102,103], [100,101,102], [102, 103]
        self.assertEqual(self.solution.numOfSubarrays(arr), 6)

    def test_modulo_constraint(self):
        """Test that result follows the modulo constraint"""
        # Create a large array that would produce a result > 10^9
        arr = [1] * 10**5  # Array of 100000 ones
        result = self.solution.numOfSubarrays(arr)
        self.assertLess(result, 10**9 + 7)
        self.assertGreaterEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
