from lc_1353_maximum_number_of_events_that_can_be_attended import max_events


def test_max_events():
    assert max_events([[1, 2], [2, 3], [3, 4]]) == 3
    assert max_events([[1, 2], [2, 3], [3, 4], [1, 2]]) == 4
