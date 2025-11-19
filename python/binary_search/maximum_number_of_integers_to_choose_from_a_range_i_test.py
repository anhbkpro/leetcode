from .maximum_number_of_integers_to_choose_from_a_range_i import Solution


def test_maximum_number_of_integers_to_choose_from_a_range_i():
    assert Solution().maxCount(banned=[1, 6, 5], n=5, maxSum=6) == 2
    assert Solution().maxCount(banned=[1, 2, 3, 4, 5, 6, 7], n=8, maxSum=1) == 0
