import unittest
from .best_sightseeing_pair import Solution


class TestMaxScoreSightseeingPair(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        """Test with the basic example where optimal pair is obvious"""
        values = [8, 1, 5, 2, 6]
        self.assertEqual(self.solution.maxScoreSightseeingPair(values), 11)  # 8 + 5 - 2

    def test_minimum_length(self):
        """Test with array of minimum length (2 elements)"""
        values = [1, 2]
        self.assertEqual(self.solution.maxScoreSightseeingPair(values), 2)  # 1 + 2 - 1

    def test_descending_values(self):
        """Test with strictly descending values"""
        values = [10, 8, 6, 4, 2]
        self.assertEqual(
            self.solution.maxScoreSightseeingPair(values), 17
        )  # 10 + 8 - 1

    def test_ascending_values(self):
        """Test with strictly ascending values"""
        values = [1, 3, 5, 7, 9]
        self.assertEqual(self.solution.maxScoreSightseeingPair(values), 15)  # 7 + 9 - 1

    def test_same_values(self):
        """Test with all same values"""
        values = [5, 5, 5, 5, 5]
        self.assertEqual(self.solution.maxScoreSightseeingPair(values), 9)  # 5 + 5 - 1

    def test_large_distance(self):
        """Test with optimal pair having large distance between indices"""
        values = [10, 2, 2, 2, 8]
        self.assertEqual(
            self.solution.maxScoreSightseeingPair(values), 14
        )  # 10 + 8 - 4

    def test_alternating_values(self):
        """Test with alternating high and low values"""
        values = [1, 8, 1, 8, 1]
        self.assertEqual(self.solution.maxScoreSightseeingPair(values), 14)  # 8 + 8 - 2

    def test_edge_case_max_values(self):
        """Test with maximum possible values"""
        values = [1000, 1000]  # Assuming 1000 is max value constraint
        self.assertEqual(
            self.solution.maxScoreSightseeingPair(values), 1999
        )  # 1000 + 1000 - 1


if __name__ == "__main__":
    unittest.main()
