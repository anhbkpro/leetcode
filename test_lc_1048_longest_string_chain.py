from lc_1048_longest_string_chain import Solution


def test_longest_str_chain():
    assert Solution.longestStrChain(words=["a", "b", "ba", "bca", "bda", "bdca"]) == 4
    assert Solution.longestStrChain(words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5
