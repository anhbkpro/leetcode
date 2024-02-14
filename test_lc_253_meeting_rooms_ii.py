from lc_253_meeting_rooms_ii import Solution


def test_min_meeting_rooms():
    assert Solution.min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert Solution.min_meeting_rooms([[7, 10], [2, 4]]) == 1
    assert Solution.min_meeting_rooms([[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]) == 4
