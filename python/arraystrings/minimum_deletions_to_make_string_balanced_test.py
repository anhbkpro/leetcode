from .minimum_deletions_to_make_string_balanced import Solution


def test_minimum_deletions():
    assert Solution().minimumDeletions("aababbab") == 2
    assert Solution().minimumDeletions("bbaaaaabb") == 2
