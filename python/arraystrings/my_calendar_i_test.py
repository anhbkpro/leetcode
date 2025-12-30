from .my_calendar_i import MyCalendar


def test_my_calendar():
    calendar = MyCalendar()
    assert calendar.book(10, 20)
    assert not calendar.book(15, 25)
    assert calendar.book(20, 30)
