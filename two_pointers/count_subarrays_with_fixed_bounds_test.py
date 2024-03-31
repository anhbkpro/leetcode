from count_subarrays_with_fixed_bounds import Solution


def test_count_sub_arrays():
    Solution.count_sub_arrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5) == 2
    Solution.count_sub_arrays(nums=[1, 1, 1, 1], minK=1, maxK=1) == 10
