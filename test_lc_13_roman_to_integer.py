from lc_13_roman_to_integer import Solution


def test_roman_to_int():
    assert Solution.romanToInt(s="III") == 3
    assert Solution.romanToInt(s="IV") == 4
    assert Solution.romanToInt(s="IX") == 9
    assert Solution.romanToInt(s="LVIII") == 58
    assert Solution.romanToInt(s="MCMXCIV") == 1994
