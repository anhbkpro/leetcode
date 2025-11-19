from .remove_k_digits import Solution


def test_removeKdigits():
    assert Solution().removeKdigits("1432219", 3) == "1219"
    assert Solution().removeKdigits("10200", 1) == "200"
    assert Solution().removeKdigits("10", 2) == "0"
    assert Solution().removeKdigits("10", 1) == "0"
