from lc_1056_confusing_number import confusing_number


def test_confusing_number():
    assert confusing_number(6) is True
    assert confusing_number(89) is True
    assert confusing_number(11) is False
