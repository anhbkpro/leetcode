from lc_1154_day_of_the_year import dayOfYear


def test_day_of_year():
    assert dayOfYear(date="2019-01-09") == 9
    assert dayOfYear(date="2019-02-10") == 41
