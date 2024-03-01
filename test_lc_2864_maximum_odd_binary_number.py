from lc_2864_maximum_odd_binary_number import Solution


def test_maximum_odd_binary_number():
    assert Solution.maximum_odd_binary_number("010") == "001"
    assert Solution.maximum_odd_binary_number("0101") == "1001"
    assert Solution.maximum_odd_binary_number("100100100") == "110000001"
