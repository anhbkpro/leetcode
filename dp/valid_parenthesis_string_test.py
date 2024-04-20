from dp.valid_parenthesis_string import Solution


def test_checkValidString():
    s = Solution()
    assert s.checkValidString("()") == True
    assert s.checkValidString("(*)") == True
    assert s.checkValidString("(*))") == True
    assert s.checkValidString("((*)") == True
    assert s.checkValidString("((**))") == True
    assert s.checkValidString("((**)))") == True
    assert s.checkValidString("((**))(") == False
