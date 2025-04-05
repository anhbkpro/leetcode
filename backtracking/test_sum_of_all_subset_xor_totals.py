import pytest
from sum_of_all_subset_xor_totals import Solution


class TestSumOfAllSubsetXORTotals:
    @pytest.fixture
    def solution(self):
        return Solution()

    def test_example1(self, solution):
        # Input: nums = [1,3]
        # Output: 6
        # Explanation: The 4 subsets of [1,3] are:
        # - The empty subset has an XOR total of 0.
        # - [1] has an XOR total of 1.
        # - [3] has an XOR total of 3.
        # - [1,3] has an XOR total of 1 XOR 3 = 2.
        # 0 + 1 + 3 + 2 = 6
        assert solution.subsetXORSum([1, 3]) == 6

    def test_example2(self, solution):
        # Input: nums = [5,1,6]
        # Output: 28
        # Explanation: The 8 subsets of [5,1,6] are:
        # - The empty subset has an XOR total of 0.
        # - [5] has an XOR total of 5.
        # - [1] has an XOR total of 1.
        # - [6] has an XOR total of 6.
        # - [5,1] has an XOR total of 5 XOR 1 = 4.
        # - [5,6] has an XOR total of 5 XOR 6 = 3.
        # - [1,6] has an XOR total of 1 XOR 6 = 7.
        # - [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
        # 0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
        assert solution.subsetXORSum([5, 1, 6]) == 28

    def test_example3(self, solution):
        # Input: nums = [3,4,5,6,7,8]
        # Output: 480
        assert solution.subsetXORSum([3, 4, 5, 6, 7, 8]) == 480

    def test_empty_array(self, solution):
        # Input: nums = []
        # Output: 0
        # Explanation: The only subset is the empty subset, which has an XOR total of 0.
        assert solution.subsetXORSum([]) == 0

    def test_single_element(self, solution):
        # Input: nums = [1]
        # Output: 1
        # Explanation: The 2 subsets of [1] are:
        # - The empty subset has an XOR total of 0.
        # - [1] has an XOR total of 1.
        # 0 + 1 = 1
        assert solution.subsetXORSum([1]) == 1

    def test_all_same(self, solution):
        # Input: nums = [1,1,1]
        # Output: 4
        # Explanation: The 8 subsets of [1,1,1] are:
        # - The empty subset has an XOR total of 0.
        # - [1] has an XOR total of 1.
        # - [1] has an XOR total of 1.
        # - [1] has an XOR total of 1.
        # - [1,1] has an XOR total of 1 XOR 1 = 0.
        # - [1,1] has an XOR total of 1 XOR 1 = 0.
        # - [1,1] has an XOR total of 1 XOR 1 = 0.
        # - [1,1,1] has an XOR total of 1 XOR 1 XOR 1 = 1.
        # 0 + 1 + 1 + 1 + 0 + 0 + 0 + 1 = 4
        assert solution.subsetXORSum([1, 1, 1]) == 4

    def test_all_zeros(self, solution):
        # Input: nums = [0,0,0]
        # Output: 0
        # Explanation: All subsets have an XOR total of 0.
        assert solution.subsetXORSum([0, 0, 0]) == 0

    def test_alternating(self, solution):
        # Input: nums = [1,0,1,0,1]
        # Output: 16
        assert solution.subsetXORSum([1, 0, 1, 0, 1]) == 16

    def test_large_numbers(self, solution):
        # Input: nums = [1000,2000,3000]
        # Output: 16352
        # Explanation: The 8 subsets of [1000,2000,3000] are:
        # - The empty subset has an XOR total of 0.
        # - [1000] has an XOR total of 1000.
        # - [2000] has an XOR total of 2000.
        # - [3000] has an XOR total of 3000.
        # - [1000,2000] has an XOR total of 1000 XOR 2000 = 2968.
        # - [1000,3000] has an XOR total of 1000 XOR 3000 = 2040.
        # - [2000,3000] has an XOR total of 2000 XOR 3000 = 1024.
        # - [1000,2000,3000] has an XOR total of 1000 XOR 2000 XOR 3000 = 3320.
        # 0 + 1000 + 2000 + 3000 + 2968 + 2040 + 1024 + 3320 = 16352
        assert solution.subsetXORSum([1000, 2000, 3000]) == 16352

    def test_negative_numbers(self, solution):
        # Input: nums = [-1,-2,-3]
        # Output: -4
        # Explanation: The 8 subsets of [-1,-2,-3] are:
        # - The empty subset has an XOR total of 0.
        # - [-1] has an XOR total of -1.
        # - [-2] has an XOR total of -2.
        # - [-3] has an XOR total of -3.
        # - [-1,-2] has an XOR total of -1 XOR -2 = 1.
        # - [-1,-3] has an XOR total of -1 XOR -3 = 2.
        # - [-2,-3] has an XOR total of -2 XOR -3 = 1.
        # - [-1,-2,-3] has an XOR total of -1 XOR -2 XOR -3 = 0.
        # 0 + (-1) + (-2) + (-3) + 1 + 2 + 1 + 0 = -4
        assert solution.subsetXORSum([-1, -2, -3]) == -4

    def test_mixed_numbers(self, solution):
        # Input: nums = [-1,0,1]
        # Output: -4
        # Explanation: The 8 subsets of [-1,0,1] are:
        # - The empty subset has an XOR total of 0.
        # - [-1] has an XOR total of -1.
        # - [0] has an XOR total of 0.
        # - [1] has an XOR total of 1.
        # - [-1,0] has an XOR total of -1 XOR 0 = -1.
        # - [-1,1] has an XOR total of -1 XOR 1 = -2.
        # - [0,1] has an XOR total of 0 XOR 1 = 1.
        # - [-1,0,1] has an XOR total of -1 XOR 0 XOR 1 = -2.
        # 0 + (-1) + 0 + 1 + (-1) + (-2) + 1 + (-2) = -4
        assert solution.subsetXORSum([-1, 0, 1]) == -4

    def test_powers_of_two(self, solution):
        # Input: nums = [1,2,4,8]
        # Output: 120
        # Explanation: The 16 subsets of [1,2,4,8] are:
        # - The empty subset has an XOR total of 0.
        # - [1] has an XOR total of 1.
        # - [2] has an XOR total of 2.
        # - [4] has an XOR total of 4.
        # - [8] has an XOR total of 8.
        # - [1,2] has an XOR total of 1 XOR 2 = 3.
        # - [1,4] has an XOR total of 1 XOR 4 = 5.
        # - [1,8] has an XOR total of 1 XOR 8 = 9.
        # - [2,4] has an XOR total of 2 XOR 4 = 6.
        # - [2,8] has an XOR total of 2 XOR 8 = 10.
        # - [4,8] has an XOR total of 4 XOR 8 = 12.
        # - [1,2,4] has an XOR total of 1 XOR 2 XOR 4 = 7.
        # - [1,2,8] has an XOR total of 1 XOR 2 XOR 8 = 11.
        # - [1,4,8] has an XOR total of 1 XOR 4 XOR 8 = 13.
        # - [2,4,8] has an XOR total of 2 XOR 4 XOR 8 = 14.
        # - [1,2,4,8] has an XOR total of 1 XOR 2 XOR 4 XOR 8 = 15.
        # 0 + 1 + 2 + 4 + 8 + 3 + 5 + 9 + 6 + 10 + 12 + 7 + 11 + 13 + 14 + 15 = 120
        assert solution.subsetXORSum([1, 2, 4, 8]) == 120
