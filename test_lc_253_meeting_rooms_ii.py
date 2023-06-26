from lc_253_meeting_rooms_ii import minMeetingRooms


def test_min_meeting_rooms():
    assert minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert minMeetingRooms([[7, 10], [2, 4]]) == 1
