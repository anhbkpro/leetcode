from .my_calendar_i import MyCalendar


def test_my_calendar():
    calendar = MyCalendar()
    assert calendar.book(10, 20) == True
    assert calendar.book(15, 25) == False
    assert calendar.book(20, 30) == True
