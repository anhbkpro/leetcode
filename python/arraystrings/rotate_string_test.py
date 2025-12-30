from .rotate_string import Solution


def test_rotate_string():
    assert Solution().rotateString("abcde", "cdeab")
    assert not Solution().rotateString("abcde", "abced")
