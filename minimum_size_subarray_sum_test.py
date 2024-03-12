from minimum_size_subarray_sum import Solution

solution = Solution()


def test_min_sub_array_len():
    assert solution.min_sub_array_len(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
    assert solution.min_sub_array_len(target=4, nums=[1, 4, 4]) == 1
    assert solution.min_sub_array_len(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]) == 0
