from minimum_common_value import Solution


def test_get_common():
    assert Solution.get_common(nums1=[1, 2, 3, 4, 5], nums2=[6, 7, 8, 9, 10]) == -1
    assert Solution.get_common(nums1=[1, 2, 3, 4, 5], nums2=[5, 6, 7, 8, 9]) == 5
    assert Solution.get_common(nums1=[1, 2, 3, 4, 5], nums2=[1, 6, 7, 8, 9]) == 1
    assert Solution.get_common(nums1=[1, 2, 3], nums2=[2, 4]) == 2
    assert Solution.get_common(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5]) == 2

    assert (
        Solution.get_common_two_pointers(nums1=[1, 2, 3, 4, 5], nums2=[6, 7, 8, 9, 10])
        == -1
    )
    assert (
        Solution.get_common_two_pointers(nums1=[1, 2, 3, 4, 5], nums2=[5, 6, 7, 8, 9])
        == 5
    )
    assert (
        Solution.get_common_two_pointers(nums1=[1, 2, 3, 4, 5], nums2=[1, 6, 7, 8, 9])
        == 1
    )
    assert Solution.get_common_two_pointers(nums1=[1, 2, 3], nums2=[2, 4]) == 2
    assert Solution.get_common_two_pointers(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5]) == 2
