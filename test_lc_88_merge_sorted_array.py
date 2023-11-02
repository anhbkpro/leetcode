from lc_88_merge_sorted_array import Solution


def test_merge():
    nums1 = [1, 2, 3, 0, 0, 0]
    Solution.merge(nums1=nums1, m=3, nums2=[2, 5, 6], n=3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    Solution.merge(nums1=nums1, m=1, nums2=[], n=0)
    assert nums1 == [1]

    nums1 = [0]
    Solution.merge(nums1=nums1, m=0, nums2=[1], n=1)
    assert nums1 == [1]
