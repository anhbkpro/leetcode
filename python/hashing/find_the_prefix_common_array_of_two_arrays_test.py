import unittest

from .find_the_prefix_common_array_of_two_arrays import Solution


class TestPrefixCommonArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        A = [1, 2, 3]
        B = [2, 1, 3]
        expected = [0, 2, 3]
        result = self.solution.findThePrefixCommonArray(A, B)
        self.assertEqual(result, expected)

    def test_all_same_elements(self):
        A = [1, 2, 3, 4]
        B = [1, 2, 3, 4]
        expected = [1, 2, 3, 4]
        result = self.solution.findThePrefixCommonArray(A, B)
        self.assertEqual(result, expected)

    def test_no_common_elements_until_end(self):
        A = [1, 2, 3, 4]
        B = [5, 6, 7, 1]
        expected = [0, 0, 0, 1]
        result = self.solution.findThePrefixCommonArray(A, B)
        self.assertEqual(result, expected)

    def test_repeated_elements(self):
        A = [1, 1, 2, 3]
        B = [1, 2, 1, 3]
        expected = [1, 0, 1, 2]
        result = self.solution.findThePrefixCommonArray(A, B)
        self.assertEqual(result, expected)

    def test_single_element(self):
        A = [1]
        B = [1]
        expected = [1]
        result = self.solution.findThePrefixCommonArray(A, B)
        self.assertEqual(result, expected)

    def test_empty_arrays(self):
        A = []
        B = []
        expected = []
        result = self.solution.findThePrefixCommonArray(A, B)
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        A = [1000000, 999999, 999998]
        B = [999999, 1000000, 999998]
        expected = [0, 2, 3]
        result = self.solution.findThePrefixCommonArray(A, B)
        self.assertEqual(result, expected)

    def test_alternating_pattern(self):
        A = [1, 3, 5, 7]
        B = [2, 4, 6, 7]
        expected = [0, 0, 0, 1]
        result = self.solution.findThePrefixCommonArray(A, B)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
