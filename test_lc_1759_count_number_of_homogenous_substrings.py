from lc_1759_count_number_of_homogenous_substrings import Solution


def test_count_homogenous():
    assert Solution.countHomogenous(s="abbcccaa") == 13
    assert Solution.countHomogenous(s="xy") == 2
