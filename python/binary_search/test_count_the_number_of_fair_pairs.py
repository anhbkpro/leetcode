from typing import List

import pytest

from binary_search.count_the_number_of_fair_pairs import Solution


@pytest.fixture
def fair_pairs_solution() -> Solution:
    return Solution()


def test_find_lower_bound_standard_case(fair_pairs_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 2, 3, 4, 5]
    input_element: int = 3
    expected_index: int = 2  # Index where 3 should be found

    # Act
    actual_index: int = fair_pairs_solution.lower_bound(
        input_nums, 0, len(input_nums) - 1, input_element
    )

    # Assert
    assert actual_index == expected_index


def test_find_lower_bound_element_not_present(fair_pairs_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 2, 4, 5]
    input_element: int = 3
    expected_index: int = 2  # Index where 3 would be inserted

    # Act
    actual_index: int = fair_pairs_solution.lower_bound(
        input_nums, 0, len(input_nums) - 1, input_element
    )

    # Assert
    assert actual_index == expected_index


def test_count_fair_pairs_standard_case(fair_pairs_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [0, 1, 7, 4, 4, 5]
    input_lower: int = 3
    input_upper: int = 6
    expected_count: int = 6  # Pairs: (0,4), (0,4), (0,5), (1,4), (1,4), (1,5)

    # Act
    actual_count: int = fair_pairs_solution.countFairPairs(
        input_nums, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count


def test_count_fair_pairs_no_valid_pairs(fair_pairs_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 2, 3]
    input_lower: int = 10
    input_upper: int = 20
    expected_count: int = 0  # No pairs sum within range [10, 20]

    # Act
    actual_count: int = fair_pairs_solution.countFairPairs(
        input_nums, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count


def test_count_fair_pairs_with_negative_numbers(fair_pairs_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [-1, -2, 3, 4]
    input_lower: int = 2
    input_upper: int = 3
    expected_count: int = 3  # Pairs: (-1,3), (-2,4), (3,-1)

    # Act
    actual_count: int = fair_pairs_solution.countFairPairs(
        input_nums, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count


def test_count_fair_pairs_with_duplicate_numbers(fair_pairs_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 1, 1, 1]
    input_lower: int = 2
    input_upper: int = 2
    expected_count: int = 6  # All pairs sum to 2

    # Act
    actual_count: int = fair_pairs_solution.countFairPairs(
        input_nums, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count


def test_count_fair_pairs_with_minimum_array(fair_pairs_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 2]
    input_lower: int = 3
    input_upper: int = 3
    expected_count: int = 1  # Only pair sums to 3

    # Act
    actual_count: int = fair_pairs_solution.countFairPairs(
        input_nums, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count


def test_count_fair_pairs_with_wide_range(fair_pairs_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 2, 3, 4, 5]
    input_lower: int = 1
    input_upper: int = 10
    expected_count: int = 10  # All possible pairs sum within range

    # Act
    actual_count: int = fair_pairs_solution.countFairPairs(
        input_nums, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count


def test_find_lower_bound_with_all_same_elements(fair_pairs_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [2, 2, 2, 2]
    input_element: int = 2
    expected_index: int = 0  # First occurrence of 2

    # Act
    actual_index: int = fair_pairs_solution.lower_bound(
        input_nums, 0, len(input_nums) - 1, input_element
    )

    # Assert
    assert actual_index == expected_index
