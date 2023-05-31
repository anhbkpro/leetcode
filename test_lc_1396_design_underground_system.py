from lc_1396_design_underground_system import UndergroundSystem


def test_design_underground_system():
    obj = UndergroundSystem()
    obj.checkIn(45, 'Leyton', 3)
    obj.checkIn(32, 'Paradise', 8)
    obj.checkIn(27, 'Leyton', 10)
    obj.checkOut(45, 'Waterloo', 15)
    obj.checkOut(27, 'Waterloo', 20)
    obj.checkOut(32, 'Cambridge', 22)
    assert obj.getAverageTime('Paradise', 'Cambridge') == 14.0
    assert obj.getAverageTime('Leyton', 'Waterloo') == 11.0
    obj.checkIn(10, 'Leyton', 24)
    assert obj.getAverageTime('Leyton', 'Waterloo') == 11.0
    obj.checkOut(10, 'Waterloo', 38)
    assert obj.getAverageTime('Leyton', 'Waterloo') == 12.0
