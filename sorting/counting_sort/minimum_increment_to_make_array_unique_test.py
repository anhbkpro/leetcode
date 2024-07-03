from .minimum_increment_to_make_array_unique import Solution


def test_min_increment_for_unique():
    assert Solution().minIncrementForUnique([1, 2, 2]) == 1
    assert Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7]) == 6
