from lc_2849_determine_if_a_cell_is_reachable_at_a_given_time import Solution


def test_is_reachable_at_time():
    assert Solution.isReachableAtTime(sx=2, sy=4, fx=7, fy=7, t=6) is True
    assert Solution.isReachableAtTime(sx=3, sy=1, fx=7, fy=3, t=3) is False
