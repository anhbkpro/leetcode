from .merge_two_2d_arrays_by_summing_values import Solution


def test_merge_arrays():
    # Test case 1: Basic case with overlapping ids
    nums1 = [[1, 2], [2, 3], [4, 5]]
    nums2 = [[1, 4], [3, 2], [4, 1]]
    expected = [[1, 6], [2, 3], [3, 2], [4, 6]]
    assert Solution().mergeArrays(nums1, nums2) == expected

    # Test case 2: No overlapping ids
    nums1 = [[1, 2], [3, 4]]
    nums2 = [[2, 3], [4, 5]]
    expected = [[1, 2], [2, 3], [3, 4], [4, 5]]
    assert Solution().mergeArrays(nums1, nums2) == expected

    # Test case 3: One empty array
    nums1 = [[1, 2], [2, 3]]
    nums2 = []
    expected = [[1, 2], [2, 3]]
    assert Solution().mergeArrays(nums1, nums2) == expected

    # Test case 4: Both empty arrays
    assert Solution().mergeArrays([], []) == []
