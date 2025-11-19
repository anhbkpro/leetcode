import unittest
from heaps.find_median_from_data_stream import MedianFinder


class TestMedianFinder(unittest.TestCase):
    def setUp(self):
        self.finder = MedianFinder()

    def test_example_1(self):
        # Test case from LeetCode example
        self.finder.addNum(1)
        self.assertEqual(self.finder.findMedian(), 1.0)
        self.finder.addNum(2)
        self.assertEqual(self.finder.findMedian(), 1.5)
        self.finder.addNum(3)
        self.assertEqual(self.finder.findMedian(), 2.0)

    def test_even_number_of_elements(self):
        # Test with even number of elements
        numbers = [2, 4, 6, 8]
        for num in numbers:
            self.finder.addNum(num)
        self.assertEqual(self.finder.findMedian(), 5.0)  # (4 + 6) / 2

    def test_odd_number_of_elements(self):
        # Test with odd number of elements
        numbers = [1, 3, 5, 7, 9]
        for num in numbers:
            self.finder.addNum(num)
        self.assertEqual(self.finder.findMedian(), 5.0)  # Middle element

    def test_unordered_elements(self):
        # Test with unordered elements
        numbers = [5, 2, 8, 1, 9]
        for num in numbers:
            self.finder.addNum(num)
        self.assertEqual(self.finder.findMedian(), 5.0)  # Middle element after sorting

    def test_duplicate_elements(self):
        # Test with duplicate elements
        numbers = [1, 1, 2, 2, 3]
        for num in numbers:
            self.finder.addNum(num)
        self.assertEqual(
            self.finder.findMedian(), 2.0
        )  # Middle element with duplicates

    def test_single_element(self):
        # Test with single element
        self.finder.addNum(5)
        self.assertEqual(self.finder.findMedian(), 5.0)

    def test_negative_numbers(self):
        # Test with negative numbers
        numbers = [-5, -2, 0, 1, 3]
        for num in numbers:
            self.finder.addNum(num)
        self.assertEqual(self.finder.findMedian(), 0.0)  # Middle element with negatives


if __name__ == "__main__":
    unittest.main()
