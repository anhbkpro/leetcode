from lc_2009_minimum_number_of_operations_to_make_array_continuous import Solution


def test_min_operations():
    assert Solution.minOperations(nums=[4, 2, 5, 3]) == 0
    assert Solution.minOperations(nums=[1, 2, 3, 5, 6]) == 1
    assert Solution.minOperations(nums=[1, 10, 100, 1000]) == 3
