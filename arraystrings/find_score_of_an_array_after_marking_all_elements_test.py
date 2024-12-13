from .find_score_of_an_array_after_marking_all_elements import Solution


def test_find_score():
    assert Solution().findScore(nums=[2, 1, 3, 4, 5, 2]) == 7
    assert Solution().findScore(nums=[2, 3, 5, 1, 3, 2]) == 5
