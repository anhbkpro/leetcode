import unittest

from .summary_ranges import Solution


class TestSummaryRanges(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test example case with multiple ranges"""
        nums = [0, 1, 2, 4, 5, 7]
        expected = ["0->2", "4->5", "7"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_example_2(self):
        """Test example case with single numbers and ranges"""
        nums = [0, 2, 3, 4, 6, 8, 9]
        expected = ["0", "2->4", "6", "8->9"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_empty_array(self):
        """Test with empty array"""
        nums = []
        expected = []
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_single_number(self):
        """Test with single number"""
        nums = [1]
        expected = ["1"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_all_consecutive(self):
        """Test when all numbers form a single range"""
        nums = [1, 2, 3, 4, 5]
        expected = ["1->5"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_no_ranges(self):
        """Test when no numbers form a range"""
        nums = [1, 3, 5, 7, 9]
        expected = ["1", "3", "5", "7", "9"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-5, -4, -3, -1, 0, 2]
        expected = ["-5->-3", "-1->0", "2"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_large_numbers(self):
        """Test with large numbers"""
        nums = [2147483646, 2147483647]
        expected = ["2147483646->2147483647"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_alternating_ranges(self):
        """Test with alternating single numbers and ranges"""
        nums = [1, 3, 4, 5, 7, 9, 10, 11]
        expected = ["1", "3->5", "7", "9->11"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)


if __name__ == "__main__":
    unittest.main()
