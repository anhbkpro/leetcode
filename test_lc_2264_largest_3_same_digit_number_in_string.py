from lc_2264_largest_3_same_digit_number_in_string import Solution


def test_largest_good_integer():
    assert Solution.largestGoodInteger("6777133339") == "777"
    assert Solution.largestGoodInteger("2300019") == "000"
    assert Solution.largestGoodInteger("42352338") == ""
