from lc_252_meeting_rooms import canAttendMeetings


def test_can_attend_meetings():
    assert canAttendMeetings([[0, 30], [5, 10], [15, 20]]) is False
    assert canAttendMeetings([[7, 10], [2, 4]]) is True
