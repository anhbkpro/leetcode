from typing import List

import pytest

from sell_stocks.LC75__best_time_to_buy_and_sell_stock import Solution


@pytest.fixture
def stock_solution() -> Solution:
    return Solution()


def test_calculate_max_profit_with_example_case(stock_solution: Solution) -> None:
    # Arrange
    input_prices: List[int] = [7, 1, 5, 3, 6, 4]
    expected_profit: int = 5

    # Act
    actual_profit: int = stock_solution.maxProfit(input_prices)

    # Assert
    assert actual_profit == expected_profit


def test_calculate_max_profit_with_decreasing_prices(stock_solution: Solution) -> None:
    # Arrange
    input_prices: List[int] = [7, 6, 4, 3, 1]
    expected_profit: int = 0

    # Act
    actual_profit: int = stock_solution.maxProfit(input_prices)

    # Assert
    assert actual_profit == expected_profit


def test_calculate_max_profit_with_increasing_prices(stock_solution: Solution) -> None:
    # Arrange
    input_prices: List[int] = [1, 2, 3, 4, 5]
    expected_profit: int = 4

    # Act
    actual_profit: int = stock_solution.maxProfit(input_prices)

    # Assert
    assert actual_profit == expected_profit


def test_calculate_max_profit_with_single_price(stock_solution: Solution) -> None:
    # Arrange
    input_prices: List[int] = [1]
    expected_profit: int = 0

    # Act
    actual_profit: int = stock_solution.maxProfit(input_prices)

    # Assert
    assert actual_profit == expected_profit


def test_calculate_max_profit_with_empty_prices(stock_solution: Solution) -> None:
    # Arrange
    input_prices: List[int] = []
    expected_profit: int = 0

    # Act
    actual_profit: int = stock_solution.maxProfit(input_prices)

    # Assert
    assert actual_profit == expected_profit


def test_calculate_max_profit_with_same_prices(stock_solution: Solution) -> None:
    # Arrange
    input_prices: List[int] = [1, 1, 1, 1]
    expected_profit: int = 0

    # Act
    actual_profit: int = stock_solution.maxProfit(input_prices)

    # Assert
    assert actual_profit == expected_profit


def test_calculate_max_profit_with_profit_at_end(stock_solution: Solution) -> None:
    # Arrange
    input_prices: List[int] = [3, 2, 6, 5, 0, 3]
    expected_profit: int = 4

    # Act
    actual_profit: int = stock_solution.maxProfit(input_prices)

    # Assert
    assert actual_profit == expected_profit
