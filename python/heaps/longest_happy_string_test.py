from .longest_happy_string import Solution


def test_longest_happy_string():
    assert Solution().longestDiverseString(a=1, b=1, c=7) == "ccaccbcc"
    assert Solution().longestDiverseString(a=2, b=2, c=1) == "ababc"
