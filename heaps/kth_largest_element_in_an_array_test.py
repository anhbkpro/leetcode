import unittest
from heaps.kth_largest_element_in_an_array import Solution


class TestFindKthLargest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        expected = 5
        self.assertEqual(self.solution.findKthLargest(nums, k), expected)

    def test_example_2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        expected = 4
        self.assertEqual(self.solution.findKthLargest(nums, k), expected)


if __name__ == "__main__":
    unittest.main()
