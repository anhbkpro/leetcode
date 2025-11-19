import unittest
from binary_search.successful_pairs_of_spells_and_potions import Solution


class TestSuccessfulPairs(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        spells = [5, 1, 3]
        potions = [1, 2, 3, 4, 5]
        success = 7
        self.assertEqual(self.sol.successfulPairs(spells, potions, success), [4, 0, 3])

    def test_example2(self):
        spells = [3, 1, 2]
        potions = [8, 5, 8]
        success = 16
        self.assertEqual(self.sol.successfulPairs(spells, potions, success), [2, 0, 2])

    def test_all_success(self):
        spells = [10, 10]
        potions = [1, 1]
        success = 5
        self.assertEqual(self.sol.successfulPairs(spells, potions, success), [2, 2])

    def test_no_success(self):
        spells = [1, 1]
        potions = [1, 1]
        success = 10
        self.assertEqual(self.sol.successfulPairs(spells, potions, success), [0, 0])

    def test_edge_case(self):
        spells = [1]
        potions = [1]
        success = 1
        self.assertEqual(self.sol.successfulPairs(spells, potions, success), [1])


if __name__ == "__main__":
    unittest.main()
