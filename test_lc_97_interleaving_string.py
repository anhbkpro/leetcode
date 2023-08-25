from lc_97_interleaving_string import Solution


def test_is_interleave():
    assert Solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac") is True
    assert Solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc") is False
    assert Solution.isInterleave(s1="", s2="", s3="") is True
