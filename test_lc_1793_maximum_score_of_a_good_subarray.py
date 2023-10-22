from lc_1793_maximum_score_of_a_good_subarray import Solution


def test_maximum_score():
    assert Solution().maximumScore(nums=[1, 4, 3, 7, 4, 5], k=3) == 15
    assert Solution().maximumScore(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0) == 20
