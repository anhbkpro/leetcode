from .fraction_addition_and_subtraction import Solution


def test_fraction_addition():
    assert Solution().fractionAddition("-1/2+1/2") == "0/1"
    assert Solution().fractionAddition("-1/2+1/2+1/3") == "1/3"
    assert Solution().fractionAddition("1/3-1/2") == "-1/6"
