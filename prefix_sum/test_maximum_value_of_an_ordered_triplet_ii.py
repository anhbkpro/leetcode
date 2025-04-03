import pytest
from maximum_value_of_an_ordered_triplet_ii import Solution


class TestMaximumValueOfAnOrderedTripletII:
    @pytest.fixture
    def solution(self):
        return Solution()

    def test_example1(self, solution):
        nums = [12, 6, 1, 2, 7]
        assert solution.maximumTripletValue(nums) == 77

    def test_example2(self, solution):
        nums = [1, 10, 3, 4, 19]
        assert solution.maximumTripletValue(nums) == 133

    def test_example3(self, solution):
        nums = [1, 2, 3]
        assert solution.maximumTripletValue(nums) == 0

    def test_minimum_length(self, solution):
        nums = [1, 2, 3]
        assert solution.maximumTripletValue(nums) == 0

    def test_all_same(self, solution):
        nums = [1, 1, 1, 1]
        assert solution.maximumTripletValue(nums) == 0

    def test_increasing(self, solution):
        nums = [1, 2, 3, 4, 5]
        assert solution.maximumTripletValue(nums) == 0

    def test_decreasing(self, solution):
        nums = [5, 4, 3, 2, 1]
        assert solution.maximumTripletValue(nums) == 4

    def test_peak_in_middle(self, solution):
        nums = [1, 2, 10, 2, 1]
        assert solution.maximumTripletValue(nums) == 8

    def test_peak_at_start(self, solution):
        nums = [10, 2, 1, 2, 3]
        assert solution.maximumTripletValue(nums) == 27

    def test_peak_at_end(self, solution):
        nums = [1, 2, 3, 2, 10]
        assert solution.maximumTripletValue(nums) == 10

    def test_negative_values(self, solution):
        nums = [-1, 2, -3, 4, -5]
        assert solution.maximumTripletValue(nums) == 20

    def test_mixed_values(self, solution):
        nums = [1, -2, 3, -4, 5]
        assert solution.maximumTripletValue(nums) == 35

    def test_large_values(self, solution):
        nums = [1000, 1, 1000]
        assert solution.maximumTripletValue(nums) == 999000

    def test_empty_array(self, solution):
        nums = []
        assert solution.maximumTripletValue(nums) == 0

    def test_single_element(self, solution):
        nums = [1]
        assert solution.maximumTripletValue(nums) == 0

    def test_two_elements(self, solution):
        nums = [1, 2]
        assert solution.maximumTripletValue(nums) == 0

    def test_alternating_values(self, solution):
        nums = [1, 10, 1, 10, 1, 10]
        assert solution.maximumTripletValue(nums) == 90

    def test_negative_peak(self, solution):
        nums = [-1, -2, -3, -2, -1]
        assert solution.maximumTripletValue(nums) == 0
