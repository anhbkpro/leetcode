from lc_2542_maximum_subsequence_score import maxScore


def test_max_score():
    assert maxScore(nums1=[1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3) == 12
    assert maxScore(nums1=[4, 2, 3, 1, 1], nums2=[7, 5, 10, 9, 6], k=1) == 30
