from lc_2870_minimum_number_of_operations_to_make_array_empty import Solution


def test_min_operations():
    assert Solution().minOperations(nums=[2, 3, 3, 2, 2, 4, 2, 3, 4]) == 4
    assert Solution().minOperations(nums=[2, 1, 2, 2, 3, 3]) == -1
