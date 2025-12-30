import unittest

from .count_complete_subarrays_in_an_array import Solution


class TestCountCompleteSubarrays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # nums = [1,3,1,2,2]
        # distinct elements = {1,2,3}
        # complete subarrays:
        # [1,3,1,2], [1,3,1,2,2], [3,1,2], [3,1,2,2]
        nums = [1, 3, 1, 2, 2]
        self.assertEqual(self.solution.countCompleteSubarrays(nums), 4)

    def test_example_2(self):
        # nums = [5,5,5,5]
        # distinct elements = {5}
        # all subarrays are complete since they all contain 5
        nums = [5, 5, 5, 5]
        self.assertEqual(self.solution.countCompleteSubarrays(nums), 10)

    def test_minimal_array(self):
        # Single element array
        nums = [1]
        self.assertEqual(self.solution.countCompleteSubarrays(nums), 1)

    def test_all_distinct(self):
        # All elements are distinct
        # [1,2,3] needs all elements to be complete
        nums = [1, 2, 3]
        self.assertEqual(self.solution.countCompleteSubarrays(nums), 1)

    def test_repeated_elements_with_gaps(self):
        # nums = [1,2,1,3,2]
        # distinct elements = {1,2,3}
        nums = [1, 2, 1, 3, 2]
        self.assertEqual(self.solution.countCompleteSubarrays(nums), 5)

    def test_two_distinct_elements(self):
        # nums = [1,2,1,2,1]
        # distinct elements = {1,2}
        nums = [1, 2, 1, 2, 1]
        self.assertEqual(self.solution.countCompleteSubarrays(nums), 10)

    def test_large_numbers(self):
        # Testing with larger values but same pattern
        nums = [100, 200, 100, 300, 200]
        self.assertEqual(self.solution.countCompleteSubarrays(nums), 5)


if __name__ == "__main__":
    unittest.main()
