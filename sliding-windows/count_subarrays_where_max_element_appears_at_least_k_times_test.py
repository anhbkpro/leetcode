from count_subarrays_where_max_element_appears_at_least_k_times import Solution


def test_count_sub_arrays():
    sol = Solution()
    assert sol.count_sub_arrays(nums=[1, 4, 2, 1], k=3) == 0
    assert sol.count_sub_arrays(nums=[1, 3, 2, 3, 3], k=2) == 6
