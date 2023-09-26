from lc_880_decoded_string_at_index import Solution


def test_decode_at_index():
    assert Solution.decode_at_index(S="leet2code3", K=10) == "o"
    assert Solution.decode_at_index(S="ha22", K=5) == "h"
    assert Solution.decode_at_index(S="a2345678999999999999999", K=1) == "a"
