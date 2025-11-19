from .separate_black_and_white_balls import Solution


def test_separate_black_and_white_balls():
    assert Solution().minimumSteps(s="0111") == 0
    assert Solution().minimumSteps(s="101") == 1
    assert Solution().minimumSteps(s="100") == 2
