from dp.valid_parenthesis_string import Solution


def test_check_valid_string():
    s = Solution()
    assert s.checkValidString("()")
    assert s.checkValidString("(*)")
    assert s.checkValidString("(*))")
    assert s.checkValidString("((*)")
    assert s.checkValidString("((**))")
    assert s.checkValidString("((**)))")
    assert not s.checkValidString("((**))(")
