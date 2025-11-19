from .maximum_score_from_removing_substrings import Solution


def test_maximum_gain():
    assert Solution().maximumGain("cdbcbbaaabab", 4, 5) == 19
    assert Solution().maximumGain("aabbaaxybbaabb", 5, 4) == 20
