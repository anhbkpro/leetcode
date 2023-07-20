from lc_1228_missing_number_in_arithmetic_progression import missing_number


def test_missing_number():
    assert missing_number(arr=[5, 7, 11, 13]) == 9
    assert missing_number(arr=[15, 13, 12]) == 14
    assert missing_number(arr=[1, 1, 1]) == 1
