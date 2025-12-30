from .my_calendar_ii import MyCalendarTwo


def test_my_calendar_two():
    calendar = MyCalendarTwo()
    assert calendar.book(10, 20)
    assert calendar.book(50, 60)
    assert calendar.book(10, 40)
    assert not calendar.book(5, 15)
    assert calendar.book(5, 10)
    assert calendar.book(25, 55)
