from lc_231_power_of_two import Solution


def test_is_power_of_two():
    assert Solution().is_power_of_two(1) == True
    assert Solution().is_power_of_two(16) == True
    assert Solution().is_power_of_two(3) == False
