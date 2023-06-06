from lc_901_online_stock_span import StockSpanner

stockSpanner = StockSpanner()


def test_next():
    assert stockSpanner.next(100) == 1
    assert stockSpanner.next(80) == 1
    assert stockSpanner.next(60) == 1
    assert stockSpanner.next(70) == 2
    assert stockSpanner.next(60) == 1
    assert stockSpanner.next(75) == 4
    assert stockSpanner.next(85) == 6
