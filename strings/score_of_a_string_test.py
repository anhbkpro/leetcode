from strings.score_of_a_string import Solution


def test_score_of_string():
    assert Solution().scoreOfString("hello") == 13
    assert Solution().scoreOfString("zaz") == 50
