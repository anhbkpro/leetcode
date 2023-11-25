from lc_1685_sum_of_absolute_differences_in_a_sorted_array import Solution


def test_get_sum_absolute_differences():
    assert Solution.getSumAbsoluteDifferences(nums=[2, 3, 5]) == [4, 3, 5]
    assert Solution.getSumAbsoluteDifferences(nums=[1, 4, 6, 8, 10]) == [24, 15, 13, 15, 21]
