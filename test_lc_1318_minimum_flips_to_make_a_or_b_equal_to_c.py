from lc_1318_minimum_flips_to_make_a_or_b_equal_to_c import minFlips


def test_min_flips():
    assert minFlips(a=2, b=6, c=5) == 3
    assert minFlips(a=4, b=2, c=7) == 1
    assert minFlips(a=1, b=2, c=3) == 0
