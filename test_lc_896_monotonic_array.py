from lc_896_monotonic_array import Solution


def test_is_monotonic():
    assert Solution.isMonotonic(nums=[1, 2, 2, 3]) is True
    assert Solution.isMonotonic(nums=[6, 5, 4, 4]) is True
    assert Solution.isMonotonic(nums=[1, 3, 2]) is False
