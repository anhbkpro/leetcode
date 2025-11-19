import pytest
from typing import List
from sliding_windows.count_the_number_of_good_subarrays import Solution


@pytest.fixture
def subarray_solution() -> Solution:
    return Solution()


def test_count_good_subarrays_with_standard_case(subarray_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 1, 1, 1, 1]
    input_k: int = 10
    expected_count: int = 1  # Only the entire array has enough pairs

    # Act
    actual_count: int = subarray_solution.countGood(input_nums, input_k)

    # Assert
    assert actual_count == expected_count


def test_count_good_subarrays_with_no_duplicates(subarray_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 2, 3, 4, 5]
    input_k: int = 1
    expected_count: int = 0  # No pairs possible with unique numbers

    # Act
    actual_count: int = subarray_solution.countGood(input_nums, input_k)

    # Assert
    assert actual_count == expected_count


def test_count_good_subarrays_with_small_k(subarray_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [3, 1, 4, 3, 2, 2, 4]
    input_k: int = 2
    expected_count: int = 4  # Multiple subarrays with at least 2 pairs

    # Act
    actual_count: int = subarray_solution.countGood(input_nums, input_k)

    # Assert
    assert actual_count == expected_count


def test_count_good_subarrays_with_single_element(subarray_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1]
    input_k: int = 1
    expected_count: int = 0  # No pairs possible with single element

    # Act
    actual_count: int = subarray_solution.countGood(input_nums, input_k)

    # Assert
    assert actual_count == expected_count


def test_count_good_subarrays_with_all_same_elements(
    subarray_solution: Solution,
) -> None:
    # Arrange
    input_nums: List[int] = [2, 2, 2, 2]
    input_k: int = 3
    expected_count: int = 3  # Multiple subarrays with enough pairs

    # Act
    actual_count: int = subarray_solution.countGood(input_nums, input_k)

    # Assert
    assert actual_count == expected_count


def test_count_good_subarrays_with_zero_k(subarray_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 2, 3, 4]
    input_k: int = 0
    expected_count: int = 20  # All possible subarrays are good when k=0

    # Act
    actual_count: int = subarray_solution.countGood(input_nums, input_k)

    # Assert
    assert actual_count == expected_count


def test_count_good_subarrays_with_alternating_elements(
    subarray_solution: Solution,
) -> None:
    # Arrange
    input_nums: List[int] = [1, 2, 1, 2, 1, 2]
    input_k: int = 2
    expected_count: int = 6  # Multiple subarrays with pairs of alternating elements

    # Act
    actual_count: int = subarray_solution.countGood(input_nums, input_k)

    # Assert
    assert actual_count == expected_count
