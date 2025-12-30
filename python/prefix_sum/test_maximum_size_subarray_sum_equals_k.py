from typing import List

import pytest

from prefix_sum.maximum_size_subarray_sum_equals_k import Solution


@pytest.fixture
def subarray_solution() -> Solution:
    return Solution()


def test_find_max_subarray_with_standard_case(subarray_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, -1, 5, -2, 3]
    input_k: int = 3
    expected_length: int = 4  # Subarray [-1, 5, -2, 3] sums to 3

    # Act
    actual_length: int = subarray_solution.max_sub_array_len(input_nums, input_k)

    # Assert
    assert actual_length == expected_length


def test_find_max_subarray_with_no_valid_subarray(subarray_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 2, 3, 4, 5]
    input_k: int = 15
    expected_length: int = 5  # No subarray sums to 15

    # Act
    actual_length: int = subarray_solution.max_sub_array_len(input_nums, input_k)

    # Assert
    assert actual_length == expected_length


def test_find_max_subarray_with_zero_sum(subarray_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, -1, 1, -1]
    input_k: int = 0
    expected_length: int = 4  # Entire array sums to 0

    # Act
    actual_length: int = subarray_solution.max_sub_array_len(input_nums, input_k)

    # Assert
    assert actual_length == expected_length


def test_find_max_subarray_with_single_element(subarray_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1]
    input_k: int = 1
    expected_length: int = 1  # Single element equals k

    # Act
    actual_length: int = subarray_solution.max_sub_array_len(input_nums, input_k)

    # Assert
    assert actual_length == expected_length


def test_find_max_subarray_with_negative_numbers(subarray_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [-2, -1, 2, 1]
    input_k: int = 1
    expected_length: int = 2  # Entire array sums to 1

    # Act
    actual_length: int = subarray_solution.max_sub_array_len(input_nums, input_k)

    # Assert
    assert actual_length == expected_length


def test_find_max_subarray_with_multiple_valid_subarrays(
    subarray_solution: Solution,
) -> None:
    # Arrange
    input_nums: List[int] = [1, 1, 1, 1]
    input_k: int = 2
    expected_length: int = 2  # Should return length of longest valid subarray

    # Act
    actual_length: int = subarray_solution.max_sub_array_len(input_nums, input_k)

    # Assert
    assert actual_length == expected_length


def test_find_max_subarray_with_empty_array(subarray_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = []
    input_k: int = 0
    expected_length: int = 0  # Empty array case

    # Act
    actual_length: int = subarray_solution.max_sub_array_len(input_nums, input_k)

    # Assert
    assert actual_length == expected_length


def test_find_max_subarray_with_all_zeros(subarray_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [0, 0, 0, 0]
    input_k: int = 0
    expected_length: int = 4  # Entire array sums to 0

    # Act
    actual_length: int = subarray_solution.max_sub_array_len(input_nums, input_k)

    # Assert
    assert actual_length == expected_length
