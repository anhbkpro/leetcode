from .my_calendar_ii import MyCalendarTwo


def test_my_calendar_two():
    calendar = MyCalendarTwo()
    assert calendar.book(10, 20) == True
    assert calendar.book(50, 60) == True
    assert calendar.book(10, 40) == True
    assert calendar.book(5, 15) == False
    assert calendar.book(5, 10) == True
    assert calendar.book(25, 55) == True
