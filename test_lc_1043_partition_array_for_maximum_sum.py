from lc_1043_partition_array_for_maximum_sum import Solution


def test_max_sum_after_partitioning():
    assert Solution.maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3) == 84
    assert Solution.maxSumAfterPartitioning(arr=[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4) == 83
    assert Solution.maxSumAfterPartitioning(arr=[1], k=1) == 1
