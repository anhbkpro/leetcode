import unittest

from arraystrings.count_symmetric_integers import Solution


class TestCountSymmetricIntegers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_no_symmetric_integers(self):
        self.assertEqual(self.solution.countSymmetricIntegers(low=1, high=100), 9)

    def test_some_symmetric_integers(self):
        self.assertEqual(self.solution.countSymmetricIntegers(low=1200, high=1230), 4)

    def test_all_symmetric_integers(self):
        self.assertEqual(self.solution.countSymmetricIntegers(11, 22), 2)

    def test_edge_case_smallest_range(self):
        self.assertEqual(self.solution.countSymmetricIntegers(1, 1), 0)

    def test_edge_case_largest_range(self):
        self.assertEqual(self.solution.countSymmetricIntegers(1000, 1001), 1)


if __name__ == "__main__":
    unittest.main()
