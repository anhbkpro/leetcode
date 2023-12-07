from lc_1903_largest_odd_number_in_string import Solution


def test_largest_odd_number():
    assert Solution.largestOddNumber(num="52") == "5"
    assert Solution.largestOddNumber(num="4206") == ""
    assert Solution.largestOddNumber(num="35427") == "35427"
