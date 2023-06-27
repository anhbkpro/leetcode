from lc_346_moving_average_from_data_stream import MovingAverage
obj = MovingAverage(3)


def test_next():
    assert obj.next(1) == 1
    assert obj.next(10) == 5.5
    assert obj.next(3) == 4.666666666666667
    assert obj.next(5) == 6
