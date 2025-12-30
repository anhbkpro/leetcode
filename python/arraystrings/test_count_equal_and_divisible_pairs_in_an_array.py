from typing import List

import pytest

from arraystrings.count_equal_and_divisible_pairs_in_an_array import Solution


@pytest.fixture
def pair_solution() -> Solution:
    return Solution()


def test_count_pairs_with_standard_case(pair_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [3, 1, 2, 2, 2, 1, 3]
    input_k: int = 2
    expected_count: int = 4  # Pairs: (0,6), (2,4), (2,5), (3,4)

    # Act
    actual_count: int = pair_solution.countPairs(input_nums, input_k)

    # Assert
    assert actual_count == expected_count


def test_count_pairs_with_no_equal_numbers(pair_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 2, 3, 4, 5]
    input_k: int = 2
    expected_count: int = 0  # No pairs with equal numbers

    # Act
    actual_count: int = pair_solution.countPairs(input_nums, input_k)

    # Assert
    assert actual_count == expected_count


def test_count_pairs_with_all_same_numbers(pair_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 1, 1, 1]
    input_k: int = 2
    expected_count: int = 5  # Pairs with indices divisible by k=2

    # Act
    actual_count: int = pair_solution.countPairs(input_nums, input_k)

    # Assert
    assert actual_count == expected_count


def test_count_pairs_with_k_equals_one(pair_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 2, 1, 2]
    input_k: int = 1
    expected_count: int = 2  # All equal pairs count since any product is divisible by 1

    # Act
    actual_count: int = pair_solution.countPairs(input_nums, input_k)

    # Assert
    assert actual_count == expected_count


def test_count_pairs_with_large_k(pair_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 1, 1, 1]
    input_k: int = 10
    expected_count: int = 3  # No pairs with product divisible by 10

    # Act
    actual_count: int = pair_solution.countPairs(input_nums, input_k)

    # Assert
    assert actual_count == expected_count


def test_count_pairs_with_minimum_length(pair_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 1]
    input_k: int = 1
    expected_count: int = 1  # Single pair with minimum length array

    # Act
    actual_count: int = pair_solution.countPairs(input_nums, input_k)

    # Assert
    assert actual_count == expected_count
