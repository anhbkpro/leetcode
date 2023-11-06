from lc_1845_seat_reservation_manager import SeatManager
seat_manager = SeatManager(5)


def test_reserve():
    seat_manager.reserve()
    seat_manager.reserve()
    seat_manager.unreserve(2)
    seat = seat_manager.reserve()
    assert seat == 2
    seat = seat_manager.reserve()
    assert seat == 3
