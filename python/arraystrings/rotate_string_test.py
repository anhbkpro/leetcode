from .rotate_string import Solution


def test_rotate_string():
    assert Solution().rotateString("abcde", "cdeab") == True
    assert Solution().rotateString("abcde", "abced") == False
