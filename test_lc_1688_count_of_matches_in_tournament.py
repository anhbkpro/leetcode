from lc_1688_count_of_matches_in_tournament import Solution


def test_number_of_matches():
    assert Solution.numberOfMatches(n=7) == 6
    assert Solution.numberOfMatches(n=14) == 13
