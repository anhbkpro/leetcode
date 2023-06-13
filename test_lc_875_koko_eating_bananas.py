from lc_875_koko_eating_bananas import min_eating_speed


def test_min_eating_speed():
    assert min_eating_speed(piles=[3, 6, 7, 11], h=8) == 4
    assert min_eating_speed(piles=[30, 11, 23, 4, 20], h=5) == 30
    assert min_eating_speed(piles=[30, 11, 23, 4, 20], h=6) == 23
