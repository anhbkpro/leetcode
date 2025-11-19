from daily_array.special_array_with_x_elements_greater_than_or_equal_x import Solution


def test_special_array():
    assert Solution().specialArray([3, 5]) == 2
    assert Solution().specialArray([0, 0]) == -1
