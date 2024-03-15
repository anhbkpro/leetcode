from meeting_rooms_ii import Solution


def test_minMeetingRooms():
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert Solution().minMeetingRooms(intervals) == 2
    intervals = [[7, 10], [2, 4]]
    assert Solution().minMeetingRooms(intervals) == 1
