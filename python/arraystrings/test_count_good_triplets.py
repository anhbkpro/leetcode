import pytest
from typing import List
from arraystrings.count_good_triplets import Solution


@pytest.fixture
def triplet_solution() -> Solution:
    return Solution()


def test_count_good_triplets_with_standard_case(triplet_solution: Solution) -> None:
    # Arrange
    input_arr: List[int] = [3, 0, 1, 1, 9, 7]
    input_a: int = 7
    input_b: int = 2
    input_c: int = 3
    expected_count: int = 4  # Triplets: (3,0,1), (3,0,1), (3,1,1), (0,1,1)

    # Act
    actual_count: int = triplet_solution.countGoodTriplets(
        input_arr, input_a, input_b, input_c
    )

    # Assert
    assert actual_count == expected_count


def test_count_good_triplets_with_no_valid_triplets(triplet_solution: Solution) -> None:
    # Arrange
    input_arr: List[int] = [1, 1, 1, 1]
    input_a: int = 0
    input_b: int = 0
    input_c: int = 0
    expected_count: int = (
        4  # No triplets satisfy the conditions with 0 difference allowed
    )

    # Act
    actual_count: int = triplet_solution.countGoodTriplets(
        input_arr, input_a, input_b, input_c
    )

    # Assert
    assert actual_count == expected_count


def test_count_good_triplets_with_all_valid_triplets(
    triplet_solution: Solution,
) -> None:
    # Arrange
    input_arr: List[int] = [1, 2, 3]
    input_a: int = 10
    input_b: int = 10
    input_c: int = 10
    expected_count: int = 1  # Large bounds make all possible triplets valid

    # Act
    actual_count: int = triplet_solution.countGoodTriplets(
        input_arr, input_a, input_b, input_c
    )

    # Assert
    assert actual_count == expected_count


def test_count_good_triplets_with_minimum_length(triplet_solution: Solution) -> None:
    # Arrange
    input_arr: List[int] = [1, 2, 3]
    input_a: int = 1
    input_b: int = 1
    input_c: int = 1
    expected_count: int = 0  # No triplets satisfy the strict conditions

    # Act
    actual_count: int = triplet_solution.countGoodTriplets(
        input_arr, input_a, input_b, input_c
    )

    # Assert
    assert actual_count == expected_count


def test_count_good_triplets_with_negative_numbers(triplet_solution: Solution) -> None:
    # Arrange
    input_arr: List[int] = [-1, 0, 1, 2]
    input_a: int = 1
    input_b: int = 1
    input_c: int = 1
    expected_count: int = 0  # Triplets: (-1,0,1), (0,1,2)

    # Act
    actual_count: int = triplet_solution.countGoodTriplets(
        input_arr, input_a, input_b, input_c
    )

    # Assert
    assert actual_count == expected_count


def test_count_good_triplets_with_duplicate_values(triplet_solution: Solution) -> None:
    # Arrange
    input_arr: List[int] = [1, 1, 1, 2, 2]
    input_a: int = 0
    input_b: int = 0
    input_c: int = 1
    expected_count: int = 1  # Triplets with identical first two elements

    # Act
    actual_count: int = triplet_solution.countGoodTriplets(
        input_arr, input_a, input_b, input_c
    )

    # Assert
    assert actual_count == expected_count


def test_count_good_triplets_with_large_differences(triplet_solution: Solution) -> None:
    # Arrange
    input_arr: List[int] = [1, 5, 10, 15, 20]
    input_a: int = 5
    input_b: int = 5
    input_c: int = 10
    expected_count: int = 3  # Triplets satisfying larger difference constraints

    # Act
    actual_count: int = triplet_solution.countGoodTriplets(
        input_arr, input_a, input_b, input_c
    )

    # Assert
    assert actual_count == expected_count
