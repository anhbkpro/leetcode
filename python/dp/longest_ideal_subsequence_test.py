from dp.longest_ideal_subsequence import Solution


def test_longest_ideal_subsequence():
    assert Solution().longest_ideal_subsequence(s="acfgbd", k=2) == 4
    assert Solution().longest_ideal_subsequence(s="abcd", k=3) == 4
