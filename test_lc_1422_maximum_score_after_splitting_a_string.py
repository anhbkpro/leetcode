from lc_1422_maximum_score_after_splitting_a_string import Solution


def test_max_score():
    assert Solution.maxScore(s="011101") == 5
    assert Solution.maxScore(s="00111") == 5
