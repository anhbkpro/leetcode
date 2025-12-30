import unittest

from .k_th_smallest_in_lexicographical_order import Solution


class TestKthSmallestInLexicographicalOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        n = 13
        k = 2
        expected = 10
        self.assertEqual(self.solution.findKthNumber(n, k), expected)

    def test_first_number(self):
        n = 13
        k = 1
        expected = 1
        self.assertEqual(self.solution.findKthNumber(n, k), expected)

    def test_last_number(self):
        n = 13
        k = 13
        expected = 9
        self.assertEqual(self.solution.findKthNumber(n, k), expected)

    def test_single_digit_range(self):
        n = 5
        k = 3
        expected = 3
        self.assertEqual(self.solution.findKthNumber(n, k), expected)

    def test_power_of_ten(self):
        n = 10
        k = 3
        expected = 2
        self.assertEqual(self.solution.findKthNumber(n, k), expected)

    def test_two_digit_numbers(self):
        n = 20
        k = 5
        expected = 13
        self.assertEqual(self.solution.findKthNumber(n, k), expected)

    def test_three_digit_numbers(self):
        n = 100
        k = 10
        expected = 17
        self.assertEqual(self.solution.findKthNumber(n, k), expected)

    def test_leetcode_example(self):
        n = 13
        k = 2
        expected = 10
        self.assertEqual(self.solution.findKthNumber(n, k), expected)

    def test_large_number_small_k(self):
        n = 1000
        k = 1
        expected = 1
        self.assertEqual(self.solution.findKthNumber(n, k), expected)

    def test_large_number_large_k(self):
        n = 1000
        k = 1000
        expected = 999
        self.assertEqual(self.solution.findKthNumber(n, k), expected)

    def test_numbers_with_nines(self):
        n = 19
        k = 11
        expected = 19
        self.assertEqual(self.solution.findKthNumber(n, k), expected)

    def test_numbers_with_zeros(self):
        n = 20
        k = 12
        expected = 2
        self.assertEqual(self.solution.findKthNumber(n, k), expected)

    def test_k_equals_n(self):
        n = 50
        k = 50
        expected = 9
        self.assertEqual(self.solution.findKthNumber(n, k), expected)

    def test_very_large_input(self):
        n = 10000
        k = 5000
        result = self.solution.findKthNumber(n, k)
        # Verify the result is within valid range
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, n)
        # Verify it's the k-th number in lexicographical order
        all_numbers = []
        for i in range(1, n + 1):
            all_numbers.append(str(i))
        all_numbers.sort()
        self.assertEqual(str(result), all_numbers[k - 1])


if __name__ == "__main__":
    unittest.main()
