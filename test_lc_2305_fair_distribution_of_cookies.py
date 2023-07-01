from lc_2305_fair_distribution_of_cookies import distributeCookies


def test_distribute_cookies():
    assert distributeCookies(cookies=[8, 15, 10, 20, 8], k=2) == 31
    assert distributeCookies(cookies=[6, 1, 3, 2, 2, 4, 1, 2], k=3) == 7
