from typing import List

import pytest

from dp.LC75__coin_change import Solution


@pytest.fixture
def coin_solution() -> Solution:
    return Solution()


def test_calculate_min_coins_with_standard_case(coin_solution: Solution) -> None:
    # Arrange
    input_coins: List[int] = [1, 2, 5]
    input_amount: int = 11
    expected_coins: int = 3  # 5 + 5 + 1 = 11

    # Act
    actual_coins: int = coin_solution.coinChange(input_coins, input_amount)

    # Assert
    assert actual_coins == expected_coins


def test_calculate_min_coins_with_impossible_amount(coin_solution: Solution) -> None:
    # Arrange
    input_coins: List[int] = [2]
    input_amount: int = 3
    expected_coins: int = -1  # Cannot make 3 with only 2's

    # Act
    actual_coins: int = coin_solution.coinChange(input_coins, input_amount)

    # Assert
    assert actual_coins == expected_coins


def test_calculate_min_coins_with_zero_amount(coin_solution: Solution) -> None:
    # Arrange
    input_coins: List[int] = [1]
    input_amount: int = 0
    expected_coins: int = 0  # Empty solution for zero amount

    # Act
    actual_coins: int = coin_solution.coinChange(input_coins, input_amount)

    # Assert
    assert actual_coins == expected_coins


def test_calculate_min_coins_with_single_coin_match(coin_solution: Solution) -> None:
    # Arrange
    input_coins: List[int] = [1]
    input_amount: int = 1
    expected_coins: int = 1  # Direct match with single coin

    # Act
    actual_coins: int = coin_solution.coinChange(input_coins, input_amount)

    # Assert
    assert actual_coins == expected_coins


def test_calculate_min_coins_with_multiple_solutions(coin_solution: Solution) -> None:
    # Arrange
    input_coins: List[int] = [1, 2, 5]
    input_amount: int = 4
    expected_coins: int = 2  # Should choose 2+2 instead of 1+1+1+1

    # Act
    actual_coins: int = coin_solution.coinChange(input_coins, input_amount)

    # Assert
    assert actual_coins == expected_coins


def test_calculate_min_coins_with_large_coins(coin_solution: Solution) -> None:
    # Arrange
    input_coins: List[int] = [186, 419, 83, 408]
    input_amount: int = 6249
    expected_coins: int = 20  # Complex case with large numbers

    # Act
    actual_coins: int = coin_solution.coinChange(input_coins, input_amount)

    # Assert
    assert actual_coins == expected_coins


def test_calculate_min_coins_with_single_large_coin(coin_solution: Solution) -> None:
    # Arrange
    input_coins: List[int] = [1, 2, 5]
    input_amount: int = 100
    expected_coins: int = 20  # Should use twenty 5's

    # Act
    actual_coins: int = coin_solution.coinChange(input_coins, input_amount)

    # Assert
    assert actual_coins == expected_coins
