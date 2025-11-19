from heaps.remove_stones_to_minimize_the_total import Solution


def test_remove_stones_to_minimize_the_total():
    assert Solution().minStoneSum([5, 4, 9], 2) == 12
    assert Solution().minStoneSum([4, 3, 6, 7], 3) == 12
