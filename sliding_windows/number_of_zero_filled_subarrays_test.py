import unittest
from number_of_zero_filled_subarrays import Solution


class TestZeroFilledSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test Example 1: [1,3,0,0,2,0,0,4] should return 6"""
        nums = [1, 3, 0, 0, 2, 0, 0, 4]
        expected = 6
        result = self.solution.zeroFilledSubarray(nums)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """Test Example 2: [0,0,0,2,0,0] should return 9"""
        nums = [0, 0, 0, 2, 0, 0]
        expected = 9
        result = self.solution.zeroFilledSubarray(nums)
        self.assertEqual(result, expected)

    def test_example_3(self):
        """Test Example 3: [2,10,2019] should return 0"""
        nums = [2, 10, 2019]
        expected = 0
        result = self.solution.zeroFilledSubarray(nums)
        self.assertEqual(result, expected)

    def test_empty_array(self):
        """Test empty array should return 0"""
        nums = []
        expected = 0
        result = self.solution.zeroFilledSubarray(nums)
        self.assertEqual(result, expected)

    def test_single_zero(self):
        """Test array with single zero should return 1"""
        nums = [0]
        expected = 1
        result = self.solution.zeroFilledSubarray(nums)
        self.assertEqual(result, expected)

    def test_all_zeros(self):
        """Test array with all zeros"""
        nums = [0, 0, 0, 0]
        # Expected: 4 single zeros + 3 pairs + 2 triples + 1 quadruple = 10
        expected = 10
        result = self.solution.zeroFilledSubarray(nums)
        self.assertEqual(result, expected)

    def test_zeros_at_beginning_and_end(self):
        """Test zeros at beginning and end of array"""
        nums = [0, 0, 1, 2, 0, 0]
        # Expected: 2 zeros at start + 2 zeros at end = 4 single + 1 pair at start + 1 pair at end = 6
        expected = 6
        result = self.solution.zeroFilledSubarray(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
