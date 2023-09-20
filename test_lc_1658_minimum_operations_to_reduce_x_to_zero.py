from lc_1658_minimum_operations_to_reduce_x_to_zero import Solution


def test_min_operations():
    assert Solution.minOperations(nums=[1, 1, 4, 2, 3], x=5) == 2
    assert Solution.minOperations(nums=[5, 6, 7, 8, 9], x=4) == -1
