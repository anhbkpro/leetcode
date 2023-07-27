from lc_287_find_the_duplicate_number import Solution


def test_find_duplicate():
    assert Solution.find_duplicate(nums=[1, 3, 4, 2, 2]) == 2
    assert Solution.find_duplicate(nums=[3, 1, 3, 4, 2]) == 3
    assert Solution.find_duplicate(nums=[1, 1]) == 1
