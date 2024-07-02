from .single_number_iii import Solution


def test_single_number():
    assert Solution().singleNumber([1, 2, 1, 3, 2, 5]) == [3, 5]
    assert Solution().singleNumber([-1,0]) == [-1,0]
