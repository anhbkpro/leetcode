from minimum_number_of_arrows_to_burst_balloons import Solution


def test_findMinArrowShots():
    assert Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert Solution().findMinArrowShots([[1, 2]]) == 1
    assert Solution().findMinArrowShots([[2, 3], [2, 3]]) == 1
