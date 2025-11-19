from .permutation_in_string import Solution


def test_permutation_in_string():
    assert Solution().checkInclusion(s1="ab", s2="eidbaooo") is True
    assert Solution().checkInclusion(s1="ab", s2="eidboaoo") is False
    assert Solution().checkInclusion(s1="ab", s2="a") is False
    assert Solution().checkInclusionFreq(s1="ab", s2="eidbaooo") is True
    assert Solution().checkInclusionFreq(s1="ab", s2="eidboaoo") is False
    assert Solution().checkInclusionFreq(s1="ab", s2="a") is False
