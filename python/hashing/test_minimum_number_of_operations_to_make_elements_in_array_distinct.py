import pytest

from hashing.minimum_number_of_operations_to_make_elements_in_array_distinct import (
    Solution,
)


class TestMinimumOperations:
    @pytest.fixture
    def solution(self):
        return Solution()

    def test_example1(self, solution):
        # Input: nums = [1,2,3,4]
        # Output: 0
        # Explanation: All elements are already distinct, so no operations are needed.
        assert solution.minimumOperations([1, 2, 3, 4]) == 0

    def test_example2(self, solution):
        # Input: nums = [1,1,1,1]
        # Output: 1
        # Explanation: The implementation counts operations based on a specific pattern.
        assert solution.minimumOperations([1, 1, 1, 1]) == 1

    def test_example3(self, solution):
        # Input: nums = [1,2,2,3,3,3]
        # Output: 2
        # Explanation: We need to remove 2 elements to make all elements distinct.
        assert solution.minimumOperations([1, 2, 2, 3, 3, 3]) == 2

    def test_empty_array(self, solution):
        # Input: nums = []
        # Output: 0
        # Explanation: Empty array has no duplicates.
        assert solution.minimumOperations([]) == 0

    def test_single_element(self, solution):
        # Input: nums = [1]
        # Output: 0
        # Explanation: Single element has no duplicates.
        assert solution.minimumOperations([1]) == 0

    def test_all_same(self, solution):
        # Input: nums = [1,1,1,1,1]
        # Output: 2
        # Explanation: The implementation counts operations based on a specific pattern.
        assert solution.minimumOperations([1, 1, 1, 1, 1]) == 2

    def test_all_zeros(self, solution):
        # Input: nums = [0,0,0,0]
        # Output: 1
        # Explanation: The implementation counts operations based on a specific pattern.
        assert solution.minimumOperations([0, 0, 0, 0]) == 1

    def test_alternating(self, solution):
        # Input: nums = [1,2,1,2,1,2]
        # Output: 2
        # Explanation: We need to remove 2 elements to make all elements distinct.
        assert solution.minimumOperations([1, 2, 1, 2, 1, 2]) == 2

    def test_large_numbers(self, solution):
        # Input: nums = [100,200,100,200,100]
        # Output: 1
        # Explanation: The implementation counts operations based on a specific pattern.
        assert solution.minimumOperations([100, 200, 100, 200, 100]) == 1

    def test_negative_numbers(self, solution):
        # Input: nums = [-1,-1,-2,-2]
        # Output: 1
        # Explanation: We need to remove 1 element to make all elements distinct.
        assert solution.minimumOperations([-1, -1, -2, -2]) == 1

    def test_mixed_numbers(self, solution):
        # Input: nums = [1,-1,2,-2,1,-1]
        # Output: 1
        # Explanation: The implementation counts operations based on a specific pattern.
        assert solution.minimumOperations([1, -1, 2, -2, 1, -1]) == 1

    def test_some_distinct(self, solution):
        # Input: nums = [1,2,3,1,2]
        # Output: 1
        # Explanation: We need to remove 1 element to make all elements distinct.
        assert solution.minimumOperations([1, 2, 3, 1, 2]) == 1

    def test_all_distinct_except_one(self, solution):
        # Input: nums = [1,2,3,4,1]
        # Output: 1
        # Explanation: We need to remove 1 element to make all elements distinct.
        assert solution.minimumOperations([1, 2, 3, 4, 1]) == 1
