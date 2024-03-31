from count_subarrays_with_fixed_bounds import Solution


def test_count_sub_arrays():
    assert Solution.count_sub_arrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5) == 2
    assert Solution.count_sub_arrays(nums=[1, 1, 1, 1], minK=1, maxK=1) == 10
