from .make_two_arrays_equal_by_reversing_subarrays import Solution


def test_can_be_equal():
    assert Solution().canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]) is True
