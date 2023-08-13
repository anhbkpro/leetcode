from lc_2369_check_if_there_is_a_valid_partition_for_the_array_space_optimized_bottom_up import Solution


def test_valid_partition():
    assert Solution.validPartition(nums=[4, 4, 4, 5, 6]) is True
    assert Solution.validPartition(nums=[1, 1, 1, 2]) is False
