from .minimum_number_of_moves_to_seat_everyone import Solution


def test_minMovesToSeat():
    assert Solution().minMovesToSeat([3, 1, 5], [2, 7, 4]) == 4
