from dp.freedom_trail import Solution


def test_freedom_trail():
    assert Solution().findRotateSteps("godding", "gd") == 4
    assert Solution().findRotateSteps("abcde", "ade") == 6
