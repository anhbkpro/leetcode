from .count_the_number_of_fair_pairs import Solution


def test_count_fair_pairs():
    assert Solution().countFairPairs(nums=[0, 1, 7, 4, 4, 5], lower=3, upper=6) == 6
    assert Solution().countFairPairs(nums=[1, 7, 9, 2, 5], lower=11, upper=11) == 1
