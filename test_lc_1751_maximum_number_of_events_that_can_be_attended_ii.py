from lc_1751_maximum_number_of_events_that_can_be_attended_ii import maxValue


def test_max_value():
    assert maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 1]], k=2) == 7
    assert maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 10]], k=2) == 10
    assert maxValue(events=[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], k=3) == 9
