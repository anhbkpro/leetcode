from lc_1165_single_row_keyboard import calculateTime


def test_calculate_time():
    assert calculateTime('abcdefghijklmnopqrstuvwxyz', 'cba') == 4
