from lc_66_plus_one import Solution


def test_plus_one():
    assert Solution.plus_one([1, 2, 3]) == [1, 2, 4]
    assert Solution.plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert Solution.plus_one([0]) == [1]
    assert Solution.plus_one([9]) == [1, 0]  # pay attention to this case
