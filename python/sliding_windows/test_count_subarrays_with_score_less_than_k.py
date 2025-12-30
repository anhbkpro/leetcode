import unittest

from .count_subarrays_with_score_less_than_k import Solution


class TestCountSubarraysWithScoreLessThanK(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        self.assertEqual(self.solution.countSubarrays([], 10), 0)

    def test_single_element_less_than_k(self):
        self.assertEqual(self.solution.countSubarrays([2], 5), 1)

    def test_single_element_equal_or_greater_than_k(self):
        self.assertEqual(self.solution.countSubarrays([5], 5), 0)
        self.assertEqual(self.solution.countSubarrays([6], 5), 0)

    def test_all_elements_same(self):
        # nums = [1,1,1], k = 5
        self.assertEqual(self.solution.countSubarrays([1, 1, 1], 5), 5)

    def test_no_valid_subarrays(self):
        # nums = [10,10,10], k = 10
        # All subarrays have score >= 10
        self.assertEqual(self.solution.countSubarrays([10, 10, 10], 10), 0)

    def test_all_subarrays_valid(self):
        # nums = [1,2], k = 10
        # All subarrays: [1], [2], [1,2] -> scores: 1,2,3*2=6 < 10
        self.assertEqual(self.solution.countSubarrays([1, 2], 10), 3)

    def test_mixed_case(self):
        # nums = [2,1,4,3], k = 10
        # Let's check all subarrays:
        # [2] -> 2*1=2 < 10
        # [1] -> 1*1=1 < 10
        # [4] -> 4*1=4 < 10
        # [3] -> 3*1=3 < 10
        # [2,1] -> 3*2=6 < 10
        # [1,4] -> 5*2=10 == 10 (not valid)
        # [4,3] -> 7*2=14 > 10 (not valid)
        # [2,1,4] -> 7*3=21 > 10 (not valid)
        # [1,4,3] -> 8*3=24 > 10 (not valid)
        # [2,1,4,3] -> 10*4=40 > 10 (not valid)
        # So valid: [2],[1],[4],[3],[2,1] => 5
        self.assertEqual(self.solution.countSubarrays([2, 1, 4, 3], 10), 5)

    def test_large_k(self):
        # All subarrays should be valid
        self.assertEqual(self.solution.countSubarrays([1, 2, 3], 100), 6)


if __name__ == "__main__":
    unittest.main()
