import pytest
from stacks_and_queues.LC75__online_stock_span import StockSpanner


def test_stock_spanner_typical():
    spanner = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    expected_spans = [1, 1, 1, 2, 1, 4, 6]
    actual_spans = [spanner.next(price) for price in prices]
    assert actual_spans == expected_spans


def test_stock_spanner_all_increasing():
    spanner = StockSpanner()
    prices = [10, 20, 30, 40, 50]
    expected_spans = [1, 2, 3, 4, 5]
    actual_spans = [spanner.next(price) for price in prices]
    assert actual_spans == expected_spans


def test_stock_spanner_all_decreasing():
    spanner = StockSpanner()
    prices = [50, 40, 30, 20, 10]
    expected_spans = [1, 1, 1, 1, 1]
    actual_spans = [spanner.next(price) for price in prices]
    assert actual_spans == expected_spans


def test_stock_spanner_single_price():
    spanner = StockSpanner()
    assert spanner.next(100) == 1


def test_stock_spanner_repeated_prices():
    spanner = StockSpanner()
    prices = [30, 30, 30, 30]
    expected_spans = [1, 2, 3, 4]
    actual_spans = [spanner.next(price) for price in prices]
    assert actual_spans == expected_spans
