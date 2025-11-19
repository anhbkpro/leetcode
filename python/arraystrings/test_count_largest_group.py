import unittest
from .count_largest_group import Solution


class TestCountLargestGroup(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # n = 13
        # Groups: [1], [2], [3], [4], [5], [6], [7], [8], [9], [10(1)], [11(2)], [12(3)], [13(4)]
        # Digit sums: 1,2,3,4,5,6,7,8,9,1,2,3,4
        # Groups by digit sum: {1:[1,10], 2:[2,11], 3:[3,12], 4:[4,13], 5:[5], 6:[6], 7:[7], 8:[8], 9:[9]}
        # Groups with size 2: [1,10], [2,11], [3,12], [4,13]
        self.assertEqual(self.solution.countLargestGroup(13), 4)

    def test_example_2(self):
        # n = 2
        # Groups: [1], [2]
        # Digit sums: 1,2
        # Each group has size 1
        self.assertEqual(self.solution.countLargestGroup(2), 2)

    def test_single_digit(self):
        # n = 9
        # Each number forms its own group
        self.assertEqual(self.solution.countLargestGroup(9), 9)

    def test_two_digit_numbers(self):
        # n = 15
        # Groups by digit sum: {1:[1,10], 2:[2,11], 3:[3,12], 4:[4,13], 5:[5,14], 6:[6,15], 7:[7], 8:[8], 9:[9]}
        self.assertEqual(self.solution.countLargestGroup(15), 6)

    def test_edge_case_1(self):
        # n = 1
        # Only one group with one element
        self.assertEqual(self.solution.countLargestGroup(1), 1)

    def test_edge_case_100(self):
        # n = 100
        # Tests a larger number with multiple digits
        result = self.solution.countLargestGroup(100)
        self.assertGreater(result, 0)


if __name__ == "__main__":
    unittest.main()
