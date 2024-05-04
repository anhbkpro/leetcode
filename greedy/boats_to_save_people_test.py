from greedy.boats_to_save_people import Solution


def test_boats_to_save_people():
    assert Solution().numRescueBoats([1, 2], 3) == 1
    assert Solution().numRescueBoats([3, 2, 2, 1], 3) == 3
    assert Solution().numRescueBoats([3, 5, 3, 4], 5) == 4
