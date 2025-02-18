import unittest
from stacks_and_queues.construct_smallest_number_from_di_string import Solution


class TestConstructSmallestNumberFromDIString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_increasing(self):
        """Test with single 'I' pattern"""
        self.assertEqual(self.solution.smallestNumber("I"), "12")

    def test_single_decreasing(self):
        """Test with single 'D' pattern"""
        self.assertEqual(self.solution.smallestNumber("D"), "21")

    def test_all_increasing(self):
        """Test with all increasing pattern 'III'"""
        self.assertEqual(self.solution.smallestNumber("III"), "1234")

    def test_all_decreasing(self):
        """Test with all decreasing pattern 'DDD'"""
        self.assertEqual(self.solution.smallestNumber("DDD"), "4321")

    def test_mixed_pattern(self):
        """Test with mixed pattern 'IDIDID'"""
        self.assertEqual(self.solution.smallestNumber("IDIDID"), "1325476")

    def test_alternating_pattern(self):
        """Test with alternating pattern 'DIDI'"""
        self.assertEqual(self.solution.smallestNumber("DIDI"), "21435")


if __name__ == "__main__":
    unittest.main()
