from .sum_of_digits_of_string_after_convert import Solution


def test_sum_of_digits_of_string_after_convert():
    assert Solution().getLucky("iiii", 1) == 36
    assert Solution().getLucky("leetcode", 2) == 6
