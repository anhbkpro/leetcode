from lc_456_132_pattern import Solution


def test_find132pattern():
    assert Solution.find132pattern(nums=[6, 12, 3, 4, 6, 11, 20]) is True
    assert Solution.find132pattern(nums=[1, 2, 3, 4]) is False
    assert Solution.find132pattern(nums=[3, 1, 4, 2]) is True
