import unittest
from .count_elements_with_maximum_frequency import Solution


class TestMaxFrequencyElements(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.maxFrequencyElements([1, 2, 2, 3, 1, 4]), 4)

    def test_example2(self):
        self.assertEqual(self.sol.maxFrequencyElements([1, 2, 3, 4, 5]), 5)

    def test_all_same(self):
        self.assertEqual(self.sol.maxFrequencyElements([7, 7, 7, 7]), 4)

    def test_single_element(self):
        self.assertEqual(self.sol.maxFrequencyElements([42]), 1)

    def test_two_max(self):
        self.assertEqual(self.sol.maxFrequencyElements([1, 1, 2, 2, 3]), 4)

    def test_large_input(self):
        nums = [1] * 50 + [2] * 50
        self.assertEqual(self.sol.maxFrequencyElements(nums), 100)


if __name__ == "__main__":
    unittest.main()
