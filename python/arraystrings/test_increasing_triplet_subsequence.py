import unittest

from arraystrings.LC75__increasing_triplet_subsequence import Solution


class TestIncreasingTripletSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        self.assertFalse(self.solution.increasingTriplet([]))

    def test_single_element(self):
        self.assertFalse(self.solution.increasingTriplet([1]))

    def test_two_elements(self):
        self.assertFalse(self.solution.increasingTriplet([1, 2]))
        self.assertFalse(self.solution.increasingTriplet([2, 1]))

    def test_valid_triplet(self):
        self.assertTrue(self.solution.increasingTriplet([1, 2, 3]))
        self.assertTrue(self.solution.increasingTriplet([1, 2, 3, 4]))
        self.assertTrue(self.solution.increasingTriplet([2, 1, 5, 0, 4, 6]))

    def test_invalid_triplet(self):
        self.assertFalse(self.solution.increasingTriplet([5, 4, 3, 2, 1]))
        self.assertFalse(self.solution.increasingTriplet([1, 1, 1, 1, 1]))
        self.assertFalse(self.solution.increasingTriplet([2, 2, 2, 2]))

    def test_edge_cases(self):
        self.assertFalse(self.solution.increasingTriplet([1, 1, 1]))
        self.assertFalse(self.solution.increasingTriplet([1, 2, 2]))
        self.assertFalse(self.solution.increasingTriplet([2, 2, 1]))

    def test_large_numbers(self):
        self.assertTrue(self.solution.increasingTriplet([1, 1000000, 2000000]))
        self.assertFalse(self.solution.increasingTriplet([2000000, 1000000, 1]))

    def test_negative_numbers(self):
        self.assertTrue(self.solution.increasingTriplet([-3, -2, -1]))
        self.assertTrue(self.solution.increasingTriplet([-1, 0, 1]))
        self.assertFalse(self.solution.increasingTriplet([-1, -1, -1]))

    def test_mixed_numbers(self):
        self.assertTrue(self.solution.increasingTriplet([-1, 0, 1, 2]))
        self.assertTrue(self.solution.increasingTriplet([-2, -1, 0, 1]))
        self.assertFalse(self.solution.increasingTriplet([-1, 0, -1, 0]))


if __name__ == "__main__":
    unittest.main()
