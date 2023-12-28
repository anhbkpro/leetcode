from lc_1531_string_compression_ii import Solution


def test_get_length_of_optimal_compression():
    assert Solution().getLengthOfOptimalCompression(s="aaabcccd", k=2) == 4
    assert Solution().getLengthOfOptimalCompression(s="aabbaa", k=2) == 2
