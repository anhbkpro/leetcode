from lc_252_meeting_rooms import can_attend_meetings


def test_can_attend_meetings():
    assert can_attend_meetings([[0, 30], [5, 10], [15, 20]]) is False
    assert can_attend_meetings([[7, 10], [2, 4]]) is True
