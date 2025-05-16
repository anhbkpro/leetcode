import pytest
from two_pointers.LC75__max_number_of_k_sum_pairs import Solution


def test_max_operations_empty_array():
    solution = Solution()
    assert solution.maxOperations([], 5) == 0
    assert solution.maxOperationsWithHashmap([], 5) == 0


def test_max_operations_single_element():
    solution = Solution()
    assert solution.maxOperations([1], 2) == 0
    assert solution.maxOperations([2], 4) == 0
    assert solution.maxOperationsWithHashmap([1], 2) == 0
    assert solution.maxOperationsWithHashmap([2], 4) == 0


def test_max_operations_no_pairs():
    solution = Solution()
    assert solution.maxOperations([1, 2, 3, 4], 10) == 0
    assert solution.maxOperations([1, 1, 1, 1], 3) == 0
    assert solution.maxOperationsWithHashmap([1, 2, 3, 4], 10) == 0
    assert solution.maxOperationsWithHashmap([1, 1, 1, 1], 3) == 0


def test_max_operations_leetcode_example():
    solution = Solution()
    nums = [1, 2, 3, 4]
    k = 5
    assert solution.maxOperations(nums, k) == 2  # (1,4) and (2,3)
    assert solution.maxOperationsWithHashmap(nums, k) == 2  # (1,4) and (2,3)


def test_max_operations_all_same_numbers():
    solution = Solution()
    nums = [2, 2, 2, 2]
    k = 4
    assert solution.maxOperations(nums, k) == 2  # (2,2) and (2,2)


def test_max_operations_negative_numbers():
    solution = Solution()
    nums = [-1, -2, -3, -4, -5]
    k = -6
    assert solution.maxOperations(nums, k) == 2  # (-1,-5) and (-2,-4)


def test_max_operations_mixed_numbers():
    solution = Solution()
    nums = [3, 1, 3, 4, 3]
    k = 6
    assert solution.maxOperations(nums, k) == 1  # (3,3)


def test_max_operations_duplicate_pairs():
    solution = Solution()
    nums = [1, 1, 1, 1]
    k = 2
    assert solution.maxOperations(nums, k) == 2  # (1,1) and (1,1)


def test_max_operations_large_numbers():
    solution = Solution()
    nums = [1000, 2000, 3000, 4000]
    k = 5000
    assert solution.maxOperations(nums, k) == 2  # (1000,4000) and (2000,3000)


def test_max_operations_zero_sum():
    solution = Solution()
    nums = [0, 0, 0, 0]
    k = 0
    assert solution.maxOperations(nums, k) == 2  # (0,0) and (0,0)
    assert solution.maxOperationsWithHashmap(nums, k) == 2  # (0,0) and (0,0)


def test_max_operations_odd_length():
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    k = 6
    assert solution.maxOperations(nums, k) == 2  # (1,5) and (2,4)
    assert solution.maxOperationsWithHashmap(nums, k) == 2  # (1,5) and (2,4)
