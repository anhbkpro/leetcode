from lc_2483_minimum_penalty_for_a_shopping_trip import Solution


def test_best_closing_time():
    assert Solution.bestClosingTime('YYNY') == 2
    assert Solution.bestClosingTime('NNNNN') == 0
    assert Solution.bestClosingTime('YYYY') == 4
