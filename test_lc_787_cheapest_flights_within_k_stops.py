from lc_787_cheapest_flights_within_k_stops import Solution


def test_find_cheapest_price():
    assert Solution.find_cheapest_price(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1) == 200
    assert Solution.find_cheapest_price(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0) == 500
