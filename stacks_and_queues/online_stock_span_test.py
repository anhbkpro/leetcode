from stacks_and_queues.online_stock_span import StockSpanner


def test_online_stock_span():
    obj = StockSpanner()
    assert obj.next(100) == 1
    assert obj.next(80) == 1
    assert obj.next(60) == 1
    assert obj.next(70) == 2
    assert obj.next(60) == 1
    assert obj.next(75) == 4
    assert obj.next(85) == 6
