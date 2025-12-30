import unittest

from simulation.water_bottles import Solution


class TestWaterBottles(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.numWaterBottles(9, 3), 13)

    def test_example2(self):
        self.assertEqual(self.sol.numWaterBottles(15, 4), 19)

    def test_no_exchange(self):
        self.assertEqual(self.sol.numWaterBottles(5, 10), 5)

    def test_one_exchange(self):
        self.assertEqual(self.sol.numWaterBottles(3, 3), 4)

    def test_large_numbers(self):
        self.assertEqual(self.sol.numWaterBottles(100, 5), 124)


if __name__ == "__main__":
    unittest.main()
