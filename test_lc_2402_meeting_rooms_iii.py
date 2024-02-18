from lc_2402_meeting_rooms_iii import Solution


def test_most_booked():
    assert Solution.most_booked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]) == 0
    assert Solution.most_booked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]) == 1
