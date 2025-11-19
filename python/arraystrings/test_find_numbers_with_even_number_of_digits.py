import unittest
from .find_numbers_with_even_number_of_digits import ConvertToString, ExtractDigits


class TestFindNumbersWithEvenNumberOfDigits(unittest.TestCase):
    def setUp(self):
        self.converter = ConvertToString()
        self.extractor = ExtractDigits()

    def test_all_even_digits(self):
        nums = [22, 4444, 6666]
        self.assertEqual(self.converter.findNumbers(nums), 3)
        self.assertEqual(self.extractor.findNumbers(nums), 3)

    def test_all_odd_digits(self):
        nums = [1, 333, 55555]
        self.assertEqual(self.converter.findNumbers(nums), 0)
        self.assertEqual(self.extractor.findNumbers(nums), 0)

    def test_mixed_digits(self):
        nums = [12, 345, 2, 6, 7896]
        # 12 and 7896 have even number of digits
        self.assertEqual(self.converter.findNumbers(nums), 2)
        self.assertEqual(self.extractor.findNumbers(nums), 2)

    def test_empty_array(self):
        nums = []
        self.assertEqual(self.converter.findNumbers(nums), 0)
        self.assertEqual(self.extractor.findNumbers(nums), 0)

    def test_single_element_even(self):
        nums = [1000]
        self.assertEqual(self.converter.findNumbers(nums), 1)
        self.assertEqual(self.extractor.findNumbers(nums), 1)

    def test_single_element_odd(self):
        nums = [123]
        self.assertEqual(self.converter.findNumbers(nums), 0)
        self.assertEqual(self.extractor.findNumbers(nums), 0)


if __name__ == "__main__":
    unittest.main()
