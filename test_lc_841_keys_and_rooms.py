from lc_841_keys_and_rooms import canVisitAllRooms


def test_can_visit_all_rooms():
    assert canVisitAllRooms(rooms=[[1], [2], [3], []]) is True
    assert canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]]) is False
