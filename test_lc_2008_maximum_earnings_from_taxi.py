from lc_2008_maximum_earnings_from_taxi import max_taxi_earnings


def test_max_taxi_earnings():
    assert max_taxi_earnings(
        n=5,
        rides=[[2, 5, 4], [1, 5, 1]]
    ) == 7
    assert max_taxi_earnings(
        n=20,
        rides=[[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]
    ) == 20
